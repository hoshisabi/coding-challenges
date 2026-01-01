using System.Runtime.InteropServices;
using AoC.Shared;

namespace AoC.Year2025;

public class Day08 : IDay
{
    public int Year => 2025;
    public int Day => 8;

    public record JunctionBox
    {
        public string Name { get; }
        public int X { get; }
        public int Y { get; }
        public int Z { get; }
        public Circuit Circuit { get; set; }
        public long CircuitSize => Circuit.Boxes.Count;

        public JunctionBox(String name, int x, int y, int z)
        {
            Name = name; X = x; Y = y; Z = z;
            // This is now safe because 'this' is available in the constructor body
            Circuit = new Circuit([this]);
        }

        public long DistanceSq(JunctionBox other)
        {
            long xd = X - other.X;
            long yd = Y - other.Y;
            long zd = Z - other.Z;
            return xd * xd + yd * yd + zd * zd;           
        }
        
        public long Distance(JunctionBox other)
        {
            return (long)Math.Floor(Math.Sqrt(DistanceSq(other)));
        }
        
        public override string ToString() => $"({X},{Y},{Z}): {Circuit.Boxes.Count}";
    }
    
    public record Circuit(HashSet<JunctionBox> Boxes)
    {
        public void AddBox(JunctionBox box)
        {
            var otherCircuit = box.Circuit;
            if (ReferenceEquals(this, otherCircuit)) return;
            foreach (var otherBox in otherCircuit.Boxes)
            {
                otherBox.Circuit = this;
                Boxes.Add(otherBox);
            }
            otherCircuit.Boxes.Clear();
        }

        public override string ToString()
        {
            return $"Circuit({Boxes.Count})";
        }
    }

    private static List<JunctionBox> GetBoxes(string[] input)
    {
        var boxes = input
            .Select(line => line.Split(',').Select(int.Parse).ToArray())
            .Select((coord, index) => new JunctionBox($"box{index}", coord[0], coord[1], coord[2]))
            .ToList();
        return boxes;
    }

    public long SolvePart1(string[] input)
    {
        var boxes = GetBoxes(input);
        var topNum = input.Length == 20 ? 10 : 1000; 
       
        var shortestPairs = boxes
            .SelectMany((boxA, index) => boxes
                .Skip(index + 1) // Ensures we only pair with subsequent items (avoids duplicates and self-pairing)
                .Select(boxB => new 
                { 
                    Box1 = boxA, 
                    Box2 = boxB, 
                    Dist = boxA.Distance(boxB) 
                }))
            .OrderBy(pair => pair.Dist)
            .Take(topNum)
            .ToList();

        foreach (var pair in shortestPairs
                     .Where(pair => !ReferenceEquals(pair.Box1.Circuit, pair.Box2.Circuit)))
        {
            pair.Box1.Circuit.AddBox(pair.Box2);
        }

        var top3Circuits = boxes
            .Select(box => box.Circuit)
            .Distinct() 
            .OrderByDescending(c => c.Boxes.Count)
            .Take(3)
            .ToList();
        var products = top3Circuits
            .Select(c => c.Boxes.Count)
            .Aggregate((acc, size) => acc * size);
        
        return products;
    }

    public long SolvePart2(string[] input)
    {
        var boxes = GetBoxes(input);

        var shortestPairs = boxes
            .SelectMany((boxA, index) => boxes
                .Skip(index + 1) // Ensures we only pair with subsequent items (avoids duplicates and self-pairing)
                .Select(boxB => new 
                { 
                    Box1 = boxA, 
                    Box2 = boxB, 
                    Dist = boxA.Distance(boxB) 
                }))
            .OrderBy(pair => pair.Dist)
            .ToList();

        var answer = -1L;
        foreach (var pair in shortestPairs.Where(pair => pair.Box1.Circuit != pair.Box2.Circuit))
        {
            answer = pair.Box1.X * pair.Box2.X;
            pair.Box2.Circuit.AddBox(pair.Box1);
        }
        
        return answer;
    }
}