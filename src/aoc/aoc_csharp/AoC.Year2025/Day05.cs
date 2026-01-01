using System.Security;
using System.Security.Cryptography;
using AoC.Shared;

namespace AoC.Year2025;

public class Day05: IDay
{
    public int Year => 2025;
    public int Day => 5;

    private class LongRange(long start, long end)
    {
        public long Start { get; set; } = start;
        public long End { get; set; } = end;
    }

    private static List<LongRange> SimplifyWithSweepLine(List<LongRange> ranges)
    {
        if (ranges.Count == 0) return [];

        // Collect all boundaries. 
        // We treat 'End' as 'End + 1' for adjacency merging (1-2 and 3-4 become 1-4)
        var starts = ranges.Select(r => r.Start).OrderBy(x => x).ToList();
        var ends = ranges.Select(r => r.End).OrderBy(x => x).ToList();

        var result = new List<LongRange>();
    
        long? currentStart = starts[0];
        int activeRanges = 0;
        int sIdx = 0;
        int eIdx = 0;

        // Process all starts and ends in order
        while (sIdx < starts.Count)
        {
            // If the next Start is before or exactly adjacent to the next End
            // (Using <= eIdx for standard overlap, or +1 logic for adjacency)
            if (starts[sIdx] <= ends[eIdx] + 1) 
            {
                if (activeRanges == 0) currentStart = starts[sIdx];
                activeRanges++;
                sIdx++;
            }
            else
            {
                activeRanges--;
                if (activeRanges == 0)
                {
                    result.Add(new LongRange(currentStart!.Value, ends[eIdx]));
                }
                eIdx++;
            }
        }

        while (eIdx < ends.Count)
        {
            activeRanges--;
            if (activeRanges == 0)
            {
                result.Add(new LongRange(currentStart!.Value, ends[eIdx]));
            }
            eIdx++;
        }

        return result;
    }    

    private static bool InRange(List<LongRange> freshRanges, long ingredient)
    {
        return freshRanges.Any(range => ingredient >= range.Start && ingredient <= range.End);
    }
    

    private static (List<LongRange> ranges, Dictionary<long, bool> ingredients) CreateIngredientsDb(string[] input)
    {
        List<LongRange> ranges = [];
        Dictionary<long, bool> ingredients = new();
        var freshRanges = true;
        
        foreach (var line in input)
        {
            
            if (line == "")
            {
                freshRanges = false;
                continue;
            }
            
            if (freshRanges)
            {
                var dashIndex = line.IndexOf('-');
                var start = long.Parse(line[..dashIndex]);
                var end = long.Parse(line[(dashIndex + 1)..]);
                ranges.Add(new LongRange(start, end));
            }
            else
            {
                var ingredient = long.Parse(line);
                ingredients.Add(ingredient, InRange(ranges, ingredient));
            }
        }

        return (ranges, ingredients);
    }

    public string SolvePart1(string[] input)
    {
        var (ranges, ingredients) = CreateIngredientsDb(input);
        return ingredients.Count(ingredient => ingredient.Value).ToString();
    }

    public string SolvePart2(string[] input)
    {
        var (ranges, ingredients) = CreateIngredientsDb(input);
        var simplifiedRange = SimplifyWithSweepLine(ranges);

        // simplification seems to be a reasonable reduction, better than 50% reduction
        return simplifiedRange.Sum(range => (range.End - range.Start + 1)).ToString();
    }
}