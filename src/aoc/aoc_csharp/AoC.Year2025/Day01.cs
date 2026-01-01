using AoC.Shared;

namespace AoC.Year2025;

public class Day01: IDay
{
    public int Year => 2025;
    public int Day => 1;
    
    private int part1Zeros;
    private int part2Zeros;

    public void solve(string[] input)
    {
        int dialPos = 50;
        part1Zeros = 0;
        part2Zeros = 0;
        foreach (var line in input)
        {
            if (line == null || line.Length < 2)
                continue;
            var direction = char.ToUpper(line[0]);
            var distance = int.Parse(line[1..]);
            if (direction == 'L')
            {
                part2Zeros += distance / 100;
                if (dialPos != 0 && (distance % 100) >= dialPos)
                    part2Zeros += 1;
                dialPos = (dialPos - distance).Mod(100);
            }
            else
            {
                part2Zeros += (dialPos + distance) / 100;
                dialPos = (dialPos + distance) % 100;
            }
            if (dialPos == 0)
                part1Zeros++;
        }
    }
    
    
    public long SolvePart1(string[] input)
    {
        solve(input);
        return part1Zeros;
    }

    public long SolvePart2(string[] input)
    {
        solve(input);
        return part2Zeros;
    }
}