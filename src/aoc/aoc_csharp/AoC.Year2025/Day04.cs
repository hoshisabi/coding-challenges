using AoC.Shared;

namespace AoC.Year2025;

public class Day04: IDay
{
    private static (int, int)[] _directions = new[]
    {
        (-1, 0), (1, 0), (0, -1), (0, 1), 
        (-1, -1), (-1, 1), (1, -1), (1, 1)
    };
    public int Year => 2025;
    public int Day => 4;



    private static char[][] AssembleGrid(string[] input)
    {
        return input.Select(x => x.ToCharArray()).ToArray();
    }

    private static int CountNeighbors(char[][] grid, int x, int y)
    {
        return _directions.Count(d =>
        {
            int nx = x + d.Item1, ny = y + d.Item2;
            return nx >= 0 && nx < grid.Length &&
                   ny >= 0 && ny < grid[nx].Length &&
                   grid[nx][ny] != '.';
        });
    }
    
    private int SolveFor(string[] input, bool repeat)
    {
        bool dirty = false;
        int total = 0;
        var grid = AssembleGrid(input);
        while (true)
        {
            dirty = false;
            for (var x = 0; x < grid.Length; x++)
            {
                for (var y = 0; y < grid[x].Length; y++)
                {
                    if (grid[x][y] == '@')
                    {
                        var neighbors = CountNeighbors(grid, x, y);
                        if (neighbors < 4) { grid[x][y] = 'x'; dirty = true;
                            total++;
                        }
                    }
                }
            }

            if (!dirty || !repeat) break;
            for (var x = 0; x < grid.Length; x++)
            {
                for (var y = 0; y < grid[x].Length; y++)
                {
                    if (grid[x][y] == 'x')
                    {
                        grid[x][y] = '.';
                    }
                }
            }
        }

        return total;
    }


    public string SolvePart1(string[] input)
    {
        return SolveFor(input, false).ToString();
    }

    public string SolvePart2(string[] input)
    {
        return SolveFor(input, true).ToString();
    }
}