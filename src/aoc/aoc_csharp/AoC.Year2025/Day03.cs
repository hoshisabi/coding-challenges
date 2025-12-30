using System.Security;
using AoC.Shared;

namespace AoC.Year2025;

public class Day03: IDay
{
    public int Year => 2025;
    public int Day => 3;

    private long solveFor(string[] input, int numberOfDigits)
    {
        long result = 0;
        foreach (var line in input)
        {
            var numbers = line.Trim()
                .Select(x => int.Parse(x.ToString()))
                .ToList();
            result += solveLine(numbers, numberOfDigits);
        }
        return result;

    }

    private long solveLine(List<int> numbers, int numberOfDigits)
    {
        long result = 0;
        var partialList = numbers;
        for (var digit = 0; digit < numberOfDigits; digit++)
        {
            var endPos = numberOfDigits - digit - 1;
            var f = partialList[..^endPos].Max();
            var fIndex = partialList.IndexOf(f);
            partialList = partialList[(fIndex + 1)..];
            result *= 10;
            result += f;
        }
        return result;
    }


    public string SolvePart1(string[] input)
    {
        return solveFor(input, 2).ToString();
    }

    public string SolvePart2(string[] input)
    {
        return solveFor(input, 12).ToString();
    }
}