package pe;

public class PE14
{
  private static long chainSize(long i)
  {
    long size = 1;

    while (i != 1)
    {
      if (i % 2 == 0)
      {
        i /= 2;
        size++;
      }
      else
      {
        i = 3 * i + 1;
        size++;
      }
    }
    return size;
  }

  public static void main(String[] args)
  {
    long longestSize = 0;
    long longestNum = 0;

    for (long i = 1; i < 1000000; i++)
    {
      long chain = chainSize(i);
      if (chain > longestSize)
      {
        longestNum = i;
        longestSize = chain;
        System.out.println("  longestNum = " + longestNum);
        System.out.println("  longestSize = " + longestSize);
      }
    }
    System.out.println("** longestNum = " + longestNum);
    System.out.println("** longestSize = " + longestSize);

  }
}

