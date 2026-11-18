using PE.Runner;

namespace PE.Problems;

// https://projecteuler.net/problem=2  Even Fibonacci numbers
// Port of src/pe/PE2.java, iterating instead of recursing.
public class Problem0002 : IProblem
{
    public int Number => 2;

    // The statement lists the terms up to 89; the even ones below 100 are 2, 8, 34.
    public IEnumerable<Check> Checks => [new("limit 100", () => SumEvenTerms(100), "44")];

    public object Solve() => SumEvenTerms(4_000_000);

    private static long SumEvenTerms(long limit)
    {
        long sum = 0;
        for (long a = 1, b = 2; a <= limit; (a, b) = (b, a + b))
        {
            if (a % 2 == 0) sum += a;
        }
        return sum;
    }
}
