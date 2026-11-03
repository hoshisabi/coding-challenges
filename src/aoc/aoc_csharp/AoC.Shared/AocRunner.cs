using System.Diagnostics;
using System.Reflection;

namespace AoC.Shared;

/// <summary>
/// Entry point for every AoC.YearNNNN project. Finds the IDay classes in the
/// calling assembly, so adding a day never means editing Program.cs.
/// </summary>
public static class AocRunner
{
    private const string Usage = """
        Usage: dotnet run -- [days] [options]

          days            Day numbers or ranges: 3   1 4 7   1-5   all
                          (default: the highest-numbered day in the project)

          -t, --test      Run only the example inputs (aoc<year>-<dd>-test*.txt)
          -r, --real      Run only the real input
                          (default: examples first, then real)
          --fetch         Download real inputs for the chosen days, then exit
          --no-warmup     Skip the untimed JIT warm-up run before real-input timing
          --print-data-path  Print the resolved input directory and exit
          -h, --help      Show this help

        Missing real input is downloaded automatically when AOC_SESSION is set.
        A <input>.expected file (line 1 = part 1, line 2 = part 2) is checked
        against the output; the exit code is 1 when a check fails or a part throws.
        """;

    private sealed record Options(List<int> Days, bool All, bool Test, bool Real, bool Fetch, bool Warmup);

    public static int Run(string[] args, Assembly? assembly = null)
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;
        try
        {
            return RunCore(args, assembly);
        }
        catch (Exception ex) when (ex is DirectoryNotFoundException or InvalidOperationException)
        {
            WriteColored(ConsoleColor.Red, ex.Message);
            return 2;
        }
    }

    private static int RunCore(string[] args, Assembly? assembly)
    {
        assembly ??= Assembly.GetEntryAssembly()
                     ?? throw new InvalidOperationException("No entry assembly; pass the assembly explicitly.");

        if (args.Any(a => a is "-h" or "--help" or "/?"))
        {
            Console.WriteLine(Usage);
            return 0;
        }

        if (args.Contains("--print-data-path"))
        {
            Console.WriteLine(EnvProvider.GetBaseDataPath());
            return 0;
        }

        Options options;
        try
        {
            options = Parse(args);
        }
        catch (ArgumentException ex)
        {
            Console.Error.WriteLine(ex.Message);
            Console.Error.WriteLine(Usage);
            return 2;
        }

        var days = Discover(assembly);
        if (days.Count == 0)
        {
            Console.WriteLine($"No IDay classes in {assembly.GetName().Name} yet. Create one with new-day.ps1.");
            return 0;
        }

        List<int> selected;
        if (options.All) selected = days.Keys.ToList();
        else if (options.Days.Count > 0) selected = options.Days;
        else selected = [days.Keys.Max()];

        var failed = false;
        foreach (var dayNumber in selected)
        {
            if (!days.TryGetValue(dayNumber, out var type))
            {
                Console.WriteLine($"Day {dayNumber:D2}: no class found (have: {string.Join(", ", days.Keys)})");
                failed = true;
                continue;
            }

            var probe = Create(type);
            if (options.Fetch)
            {
                var ok = InputFiles.TryDownload(probe.Year, probe.Day, out var message);
                Console.WriteLine($"Day {probe.Day:D2}: {message}");
                failed |= !ok;
                continue;
            }

            failed |= !RunDay(type, probe, options);
        }

        return failed ? 1 : 0;
    }

    private static Options Parse(string[] args)
    {
        var days = new List<int>();
        bool all = false, test = false, real = false, fetch = false, warmup = true;

        foreach (var arg in args)
        {
            switch (arg)
            {
                case "-t" or "--test": test = true; break;
                case "-r" or "--real": real = true; break;
                case "--fetch": fetch = true; break;
                case "--no-warmup": warmup = false; break;
                case "all" or "--all": all = true; break;
                default:
                    var dash = arg.IndexOf('-', 1);
                    if (int.TryParse(arg, out var d))
                        days.Add(d);
                    else if (dash > 0 && int.TryParse(arg[..dash], out var from) &&
                             int.TryParse(arg[(dash + 1)..], out var to) && from <= to)
                        days.AddRange(Enumerable.Range(from, to - from + 1));
                    else
                        throw new ArgumentException($"Unrecognized argument: {arg}");
                    break;
            }
        }

        // Neither flag means both.
        if (!test && !real) test = real = true;
        return new Options(days.Distinct().ToList(), all, test, real, fetch, warmup);
    }

    private static SortedDictionary<int, Type> Discover(Assembly assembly)
    {
        var result = new SortedDictionary<int, Type>();
        var candidates = assembly.GetTypes().Where(t =>
            typeof(IDay).IsAssignableFrom(t) && t is { IsClass: true, IsAbstract: false } &&
            t.GetConstructor(Type.EmptyTypes) != null);

        foreach (var type in candidates)
        {
            var day = Create(type).Day;
            if (result.TryGetValue(day, out var existing))
                throw new InvalidOperationException($"Day {day} is claimed by both {existing.Name} and {type.Name}.");
            result[day] = type;
        }
        return result;
    }

    private static IDay Create(Type type) => (IDay)Activator.CreateInstance(type)!;

    /// <returns>false when any check failed or a part threw.</returns>
    private static bool RunDay(Type type, IDay probe, Options options)
    {
        Header($"=== {probe.Year} Day {probe.Day:D2} ===");
        var ok = true;

        if (options.Test)
        {
            var tests = InputFiles.TestPaths(probe.Year, probe.Day);
            if (tests.Count == 0)
                Note($"  test  none: paste the example into {InputFiles.TestPath(probe.Year, probe.Day)}");
            foreach (var path in tests)
                ok &= RunInput(type, "test", path, warmup: false);
        }

        if (options.Real)
        {
            var path = InputFiles.RealPath(probe.Year, probe.Day);
            if (!File.Exists(path) && !InputFiles.TryDownload(probe.Year, probe.Day, out var message))
                Note($"  real  {message}");
            else
                ok &= RunInput(type, "real", path, options.Warmup);
        }

        Console.WriteLine();
        return ok;
    }

    private static bool RunInput(Type type, string kind, string path, bool warmup)
    {
        var input = File.ReadAllLines(path);
        if (input.Length == 0)
        {
            Note($"  {kind}  {Path.GetFileName(path)} is empty");
            return true;
        }

        Console.WriteLine($"  {kind}  {Path.GetFileName(path)}");
        var (expected1, expected2) = InputFiles.ReadExpected(path);

        if (warmup)
        {
            // Untimed run so the timed run measures the solution, not the JIT.
            var scratch = Create(type);
            TryInvoke(() => scratch.SolvePart1(input));
            TryInvoke(() => scratch.SolvePart2(input));
        }

        var day = Create(type);
        var ok = RunPart(1, () => day.SolvePart1(input), expected1);
        ok &= RunPart(2, () => day.SolvePart2(input), expected2);
        return ok;
    }

    private static bool RunPart(int part, Func<string> solve, string? expected)
    {
        var sw = Stopwatch.StartNew();
        string? answer = null;
        Exception? error = null;
        try
        {
            answer = solve();
        }
        catch (Exception ex)
        {
            error = ex;
        }
        sw.Stop();

        Console.Write($"    Part {part}  {sw.Elapsed.TotalMilliseconds,10:F2} ms  ");

        if (error is NotImplementedException)
        {
            Note("not implemented");
            return true;
        }
        if (error != null)
        {
            WriteColored(ConsoleColor.Red, $"{error.GetType().Name}: {error.Message}");
            // First frame with source info: the solution's own line, not the BCL's.
            var frame = new StackTrace(error, fNeedFileInfo: true).GetFrames()
                .FirstOrDefault(f => f.GetFileName() != null);
            if (frame != null)
                Note($"{"",26}at {Path.GetFileName(frame.GetFileName())}:line {frame.GetFileLineNumber()}" +
                     $" ({frame.GetMethod()?.Name})");
            return false;
        }

        if (expected == null)
        {
            Console.WriteLine(answer);
            return true;
        }
        if (answer == expected)
        {
            Console.Write(answer + "  ");
            WriteColored(ConsoleColor.Green, "✓");
            return true;
        }
        Console.Write(answer + "  ");
        WriteColored(ConsoleColor.Red, $"✗ expected {expected}");
        return false;
    }

    private static void TryInvoke(Func<string> f)
    {
        try { f(); } catch { /* reported by the timed run */ }
    }

    private static void Header(string text) => WriteColored(ConsoleColor.Cyan, text);
    private static void Note(string text) => WriteColored(ConsoleColor.DarkGray, text);

    private static void WriteColored(ConsoleColor color, string text)
    {
        var previous = Console.ForegroundColor;
        Console.ForegroundColor = color;
        Console.WriteLine(text);
        Console.ForegroundColor = previous;
    }
}
