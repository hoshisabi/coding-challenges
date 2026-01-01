namespace AoC.Shared;

public interface IDay
{
    int Year { get; }
    int Day { get; }
    long SolvePart1(string[] input);
    long SolvePart2(string[] input);
}