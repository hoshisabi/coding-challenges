package pe;

import java.util.*;

public class PE12
{
  static long getTriangleNumber(long a)
  {
    long ret = 0;
    for (long i = 1; i <= a; i++)
    {
      ret += i;
    }
    return ret;
  }

  static Set<Long> getFactors(long a)
  {
    Set<Long> ret = new TreeSet<Long>();
    for (long i = 1; i <= Math.sqrt(a); i++)
    {
      if (a % i == 0)
      {
        ret.add(i);
        ret.add(a / i);
      }
    }
    return ret;
  }

  public static void main(String[] args)
  {
    boolean done = false;
    long i = 0;
    while (!done)
    {
      long tri = getTriangleNumber(++i);
      System.out.println("getTriangleNumber(" + i + ") = " + tri);
      Set<Long> factors = getFactors(tri);
      for (Long factor : factors)
      {
        System.out.println("  factor = " + factor);
      }
      done = factors.size() > 500;
    }
    System.out.println("i = " + i);
  }
}
