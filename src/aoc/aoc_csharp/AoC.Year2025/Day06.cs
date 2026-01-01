using System.Security;
using System.Security.Cryptography;
using AoC.Shared;

namespace AoC.Year2025;

public class Day06: IDay
{
    public int Year => 2025;
    public int Day => 6;

    public (List<int[]> numbers, char[] operators) gatherRanges(string[] input)
    {
        var numbersList = new List<int[]>();
        var operators = new char[input.Length];
        foreach (var line in input)
        {
            if (line is null or "") continue;
            var parts = line.Split(' ', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
            if (line.Contains('*') || line.Contains('+'))
            {
                operators = parts.Select(part => part[0]).ToArray();
            }
            else
            {
                numbersList.Add(parts.Select(int.Parse).ToArray());
            }
        }
        return (numbersList, operators);
    }
    

    private static long GenerateSum(List<int[]> numbers, char[] operators)
    {
        var resultsArr = new long[operators.Length];
        for (var x = 0; x < operators.Length; x++)
        {
            var op = operators[x];
            resultsArr[x] = op == '*' ? 1 : 0;
            for (var y = 0; y < numbers.Count; y++)
            {
                switch (op)
                {
                    case '*': resultsArr[x] *= numbers[y][x]; break;
                    case '+': resultsArr[x] += numbers[y][x]; break;
                    default: throw new Exception("Invalid operator");
                }
            }
        }

        var sum = resultsArr.Sum();
        return sum;
    }

    public string SolvePart1(string[] input)
    {
        var numbers = new List<int[]>();
        var operators = input
            .First(row => row.Contains('*') || row.Contains('+'))
            .Where(c => c is '*' or '+')
            .ToArray();
        foreach (var line in input)
        {
            if (line is null or "") continue;
            var parts = line.Split(' ', StringSplitOptions.TrimEntries | StringSplitOptions.RemoveEmptyEntries);
            if (line.Contains('*') || line.Contains('+'))
            {
                operators = parts.Select(part => part[0]).ToArray();
            }
            else
            {
                numbers.Add(parts.Select(int.Parse).ToArray());
            }
        }

        var sum = GenerateSum(numbers, operators);
        return sum.ToString();
    }

    
    public string SolvePart2(string[] input)
    {
        var total = 0L;

        // for simplicity, assume all the lines are the same length
        List<long> numbers = [];
        int width = input[0].Length;
        for (var i = width - 1; i >= 0; i--)
        {
            var oneNumber = 0L;
            
            // This should be reset by either a digit or an operator
            // so we can detect blank columns
            var op = 'x';

            foreach (var line in input)
            {
                var c = line[i];
                if (char.IsDigit(c))
                {
                    oneNumber = (10 * oneNumber) + (c - '0');
                    op = ' ';
                }
                else if (c is '*' or '+')
                {
                    op = c;
                }
            }

            // If we got this far without having changed this, we are in a blank column
            // We should ignore it and continue onward
            if (op == 'x') continue;
    
            numbers.Add(oneNumber);
            switch (op)
            {
                case '*':
                {
                    total += numbers.Aggregate(1L, (acc, n) => acc * n);
                    numbers.Clear();
                    break;
                }
                case '+':
                {
                    total += numbers.Sum();
                    numbers.Clear();;
                    break;
                }
            }
        }
        return total.ToString();
    }
}