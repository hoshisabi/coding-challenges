using System.Diagnostics;

namespace AoC.Shared;

public static class DayRunnerExtensions
{
    public static void Run(this IDay puzzle, bool useTestData = false)
    {
        // 1. Load the data using your EnvProvider
        var fileName = $"aoc{puzzle.Year}-{puzzle.Day:D2}{(useTestData ? "-test" : "")}.txt";
        var fullPath = Path.Combine(EnvProvider.GetBaseDataPath(), puzzle.Year.ToString(), fileName);

        if (!File.Exists(fullPath))
        {
            Console.WriteLine($"Error: File not found at {fullPath}");
            return;
        }

        string[] input = File.ReadAllLines(fullPath);

        Console.WriteLine($"--- Year {puzzle.Year} Day {puzzle.Day:D2} ({(useTestData ? "TEST" : "REAL")}) ---");

        // Call the puzzle to "warm up" the JIT -- this one is ignored
        puzzle.SolvePart1(input);
        
        // 2. Execute Part 1
        ExecutePart(1, input, puzzle.SolvePart1);

        // 3. Execute Part 2
        ExecutePart(2, input, puzzle.SolvePart2);
        
        Console.WriteLine();
    }

    private static void ExecutePart(int partNumber, string[] input, Func<string[], string> solveMethod)
    {
        var sw = Stopwatch.StartNew();
        var result = solveMethod(input);
        sw.Stop();

        Console.WriteLine($"Part {partNumber} ({sw.Elapsed.TotalMilliseconds:F2} ms): {result}");
    }
}