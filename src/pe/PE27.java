package pe;

public class PE27
{
  public static void main(String[] args)
  {

    System.out.println("getMaxPrimesProduced(1, 41) = " + getMaxPrimesProduced(1, 41));
    System.out.println("getMaxPrimesProduced(79, 1601) = " + getMaxPrimesProduced(79, 1601));

    long maxPrimesProduced = 0;
    long maxA = 0;
    long maxB = 0;
    long maxPrimesProduct = 0;

    for (long a = 2; a < 1000; a++)
    {
      for (long b = 2; b < 1000; b++)
      {
        long primesProduced = getMaxPrimesProduced(a, b);
        if (primesProduced > maxPrimesProduced)
        {
          maxPrimesProduced = primesProduced;
          maxPrimesProduct = a * b;
          maxA = a;
          maxB = b;
        }
      }
    }
    System.out.println("maxA = " + maxA);
    System.out.println("maxB = " + maxB);
    System.out.println("maxPrimesProduced = " + maxPrimesProduced);
    System.out.println("maxPrimesProduct = " + maxPrimesProduct);
  }

  private static long getMaxPrimesProduced(long a, long b)
  {
    return Math.max(Math.max(getPrimesProduced(a, b), getPrimesProduced(-a, -b)),
                    Math.max(getPrimesProduced(-a, b), getPrimesProduced(a, -b)));
  }

  private static long getPrimesProduced(long a, long b)
  {
    long n = 0;
    while (true)
    {
      long result = (n * n) + (a * n) + b;
      if (!isPrime(result))
      {
        return n;
      }
      n++;
    }
  }


  @SuppressWarnings({"OverlyComplexBooleanExpression"})
  public static boolean isPrime(long n)
  {
    boolean prime = true;
    for (long i = 3; i <= Math.sqrt(n); i += 2)
    {
      if (n % i == 0)
      {
        prime = false;
        break;
      }
    }
    return n % 2 != 0 && prime && n > 2 || n == 2;
  }

}
