using AoC.Shared;

namespace AoC.Year2025;

public class Day02: IDay
{
    public int Year => 2025;
    public int Day => 2;

    private static bool IsInvalid(string id, int maxLength)
    {
        if (maxLength <= 0)
        {
            maxLength = id.Length;
        }
        for (int n = 2; n < maxLength + 1; n++)
        {
            if (id.Length % n == 0 && IsInvalidPiece(id, n))
                return true;
        }
        return false;
    }

    private static bool IsInvalidPiece(string id, int pieces)
    {
        var fragLength = id.Length / pieces;
        string idFrag = id.Substring(0, fragLength);
        var idRepeat = idFrag.Repeat(pieces);
        return idRepeat.Equals(id);
    }

    private static long CountInvalidForRange(long left, long right, int maxLength)
    {
        long count = 0;
        for (long rangeId = left; rangeId < right + 1; rangeId++)
        {
            if (IsInvalid(rangeId.ToString(), maxLength))
                count += rangeId;
        }
        return count;
    }

    private long SolveFor(string[] input, int maxLength)
    {
        long count = 0;
        foreach (var line in input)
        {
            var idList = line.Split(',');
            foreach (var id in idList)
            {
                if (id.Split('-') is [var left, var right])
                {
                    count += CountInvalidForRange(long.Parse(left), long.Parse(right), maxLength);
                }
            }
        }
        return count;
    }

    public string SolvePart1(string[] input)
    {
        return SolveFor(input, 2).ToString();
    }

    public string SolvePart2(string[] input)
    {
        return SolveFor(input, -1).ToString();
    }
}