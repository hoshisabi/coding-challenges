namespace AoC.Shared;

public static class MathExtensions
{
    // The "True" Modulo
    public static int Mod(this int a, int n) => ((a % n) + n) % n;
}