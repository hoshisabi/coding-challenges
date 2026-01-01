using AoC.Shared;

namespace AoC.Year2025;

public class Day07: IDay
{
    public int Year => 2025;
    public int Day => 7;


    public long SolvePart1(string[] input)
    {
        HashSet<int> beams = [];
        var split = 0;
        var startBeam = input[0].IndexOf('S');
        beams.Add(startBeam);
        foreach (var line in input)
        {
            foreach (var beam in beams.ToList())
            {
                
                if (line[beam] != '^') continue;
                var left = beam - 1;
                var right = beam + 1;
                split++;
                beams.Remove(beam);
                if (left >= 0) beams.Add(left);
                if (left < line.Length) beams.Add(right);
            }
        }

        return split;
    }
    
    public long SolvePart2(string[] input)
    {
        var width = input[0].Length;
        var counts = new long[width];
        var startBeam = input[0].IndexOf('S');
        counts[startBeam] = 1;
        
        foreach (var line in input)
        {
            var nextCounts = new long[width];

            for (var pos = 0; pos < width; pos++)
            {
                if (counts[pos] < 1) continue;
                if (line[pos] != '^')
                {
                    nextCounts[pos] += counts[pos];
                }
                else
                {
                    var left = pos - 1;
                    var right = pos + 1;
                    if (left >= 0)
                    {
                        nextCounts[left] += counts[pos];
                    }

                    if (right < width)
                    {
                        nextCounts[right] += counts[pos];
                    }
                }
            }
            
            counts = nextCounts;
        }
        return counts.Sum();
    }
}