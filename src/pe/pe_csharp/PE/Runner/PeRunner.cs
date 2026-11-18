using System.Diagnostics;
using System.Globalization;
using System.Reflection;

namespace PE.Runner;

/// <summary>
/// Finds the IProblem classes in this assembly, runs each one's checks, then its solve,
/// and compares the answer to data/pe/answers.txt when one is recorded.
/// </summary>
public static class PeRunner
{
    private const string Usage = """
        Usage: dotnet run -- [problems] [options]

          problems        Problem numbers or ranges: 2   2 5 9   1-10   all
                          (default: the highest-numbered problem in the project)

          -c, --checks    Run only the checks, not the solve
          --accept        Record each solved answer in answers.txt, replacing
                          any recorded one (after you have confirmed it on
                          projecteuler.net)
          --warmup        Solve once untimed before the timed solve, so the
                          timing excludes the JIT. Off by default: PE solves
                          can take minutes.
          --print-data-path  Print the data directory and exit
          -h, --help      Show this help

        A failing check skips that problem's solve. The exit code is 1 when a
        check fails, the answer differs from answers.txt, or anything throws.
        """;

    private sealed record Options(List<int> Numbers, bool All, bool ChecksOnly, bool Accept, bool Warmup);

    public static int Run(string[] args)
    {
        Console.OutputEncoding = System.Text.Encoding.UTF8;

        if (args.Any(a => a is "-h" or "--help" or "/?"))
        {
            Console.WriteLine(Usage);
            return 0;
        }

        if (args.Contains("--print-data-path"))
        {
            Console.WriteLine(PeData.DataPath);
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

        var problems = Discover();
        if (problems.Count == 0)
        {
            Console.WriteLine("No IProblem classes yet. Create one with new-problem.ps1.");
            return 0;
        }

        List<int> selected;
        if (options.All) selected = problems.Keys.ToList();
        else if (options.Numbers.Count > 0) selected = options.Numbers;
        else selected = [problems.Keys.Max()];

        var answers = PeData.ReadAnswers();
        var answersChanged = false;
        var failed = false;

        foreach (var number in selected)
        {
            if (!problems.TryGetValue(number, out var type))
            {
                Console.WriteLine($"Problem {number}: no class found (have: {string.Join(", ", problems.Keys)})");
                failed = true;
                continue;
            }

            Header($"=== Problem {number} ===  https://projecteuler.net/problem={number}");
            var (ok, answer) = RunProblem(type, options, answers.GetValueOrDefault(number));
            failed |= !ok;

            // answer is null when a check failed or the solve threw. A mismatch still records:
            // --accept means the new answer has been confirmed on the site.
            if (options.Accept && answer != null && answers.GetValueOrDefault(number) != answer)
            {
                answers[number] = answer;
                answersChanged = true;
                Note($"  recorded {answer} in {PeData.AnswersPath}");
            }
            Console.WriteLine();
        }

        if (answersChanged) PeData.WriteAnswers(answers);
        return failed ? 1 : 0;
    }

    private static Options Parse(string[] args)
    {
        var numbers = new List<int>();
        bool all = false, checksOnly = false, accept = false, warmup = false;

        foreach (var arg in args)
        {
            switch (arg)
            {
                case "-c" or "--checks": checksOnly = true; break;
                case "--accept": accept = true; break;
                case "--warmup": warmup = true; break;
                case "all" or "--all": all = true; break;
                default:
                    var dash = arg.IndexOf('-', 1);
                    if (int.TryParse(arg, out var n))
                        numbers.Add(n);
                    else if (dash > 0 && int.TryParse(arg[..dash], out var from) &&
                             int.TryParse(arg[(dash + 1)..], out var to) && from <= to)
                        numbers.AddRange(Enumerable.Range(from, to - from + 1));
                    else
                        throw new ArgumentException($"Unrecognized argument: {arg}");
                    break;
            }
        }

        return new Options(numbers.Distinct().ToList(), all, checksOnly, accept, warmup);
    }

    private static SortedDictionary<int, Type> Discover()
    {
        var result = new SortedDictionary<int, Type>();
        var candidates = Assembly.GetExecutingAssembly().GetTypes().Where(t =>
            typeof(IProblem).IsAssignableFrom(t) && t is { IsClass: true, IsAbstract: false } &&
            t.GetConstructor(Type.EmptyTypes) != null);

        foreach (var type in candidates)
        {
            var number = Create(type).Number;
            if (result.TryGetValue(number, out var existing))
                throw new InvalidOperationException($"Problem {number} is claimed by both {existing.Name} and {type.Name}.");
            result[number] = type;
        }
        return result;
    }

    private static IProblem Create(Type type) => (IProblem)Activator.CreateInstance(type)!;

    /// <returns>ok = no check failed, nothing threw, and the answer matched any recorded one.</returns>
    private static (bool Ok, string? Answer) RunProblem(Type type, Options options, string? recorded)
    {
        var checks = Create(type).Checks.ToList();
        var width = checks.Count == 0 ? 5 : Math.Max(5, checks.Max(c => c.Label.Length));

        var checksOk = true;
        foreach (var check in checks)
            checksOk &= Report($"check  {check.Label.PadRight(width)}", check.Compute, check.Expected);

        if (options.ChecksOnly) return (checksOk, null);
        if (!checksOk)
        {
            Note($"  solve  {"".PadRight(width)}skipped: a check failed");
            return (false, null);
        }

        if (options.Warmup)
        {
            var scratch = Create(type);
            try { scratch.Solve(); } catch { /* reported by the timed run */ }
        }

        var problem = Create(type);
        string? answer = null;
        var ok = Report($"solve  {"".PadRight(width)}", () => answer = Format(problem.Solve()), recorded,
            recordedAnswer: true);
        return (ok, answer);
    }

    /// <returns>false when the value threw or differs from <paramref name="expected"/>.</returns>
    private static bool Report(string label, Func<object> compute, string? expected, bool recordedAnswer = false)
    {
        var sw = Stopwatch.StartNew();
        string? value = null;
        Exception? error = null;
        try
        {
            value = Format(compute());
        }
        catch (Exception ex)
        {
            error = ex;
        }
        sw.Stop();

        Console.Write($"  {label}  {FormatElapsed(sw.Elapsed),10}  ");

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
                Note($"{"",14}at {Path.GetFileName(frame.GetFileName())}:line {frame.GetFileLineNumber()}" +
                     $" ({frame.GetMethod()?.Name})");
            return false;
        }

        Console.Write(value + "  ");
        if (expected == null)
        {
            Console.WriteLine();
            return true;
        }
        if (value == expected)
        {
            WriteColored(ConsoleColor.Green, recordedAnswer ? "✓ matches answers.txt" : "✓");
            return true;
        }
        WriteColored(ConsoleColor.Red, $"✗ expected {expected}");
        return false;
    }

    private static string Format(object value) => Convert.ToString(value, CultureInfo.InvariantCulture) ?? "";

    private static string FormatElapsed(TimeSpan t) =>
        t.TotalSeconds >= 10 ? $"{t.TotalSeconds:F1} s" : $"{t.TotalMilliseconds:F2} ms";

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
