namespace AoC.Shared;

public interface IDay
{
    int Year { get; }
    int Day { get; }
    string SolvePart1(string[] input);
    string SolvePart2(string[] input);
}