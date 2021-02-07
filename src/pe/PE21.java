package pe;

import java.util.*;

public class PE21
{
  private static final int LIMIT = 10000;
  private static Set<Long> amicableNumbers = new TreeSet<Long>();

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
    ret.remove(a);
    return ret;
  }

  static long sumOfFactors(long number)
  {
    Set<Long> factors = getFactors(number);
    long sum = 0;
//    System.out.println("  number = " + number);
    for (Long factor : factors)
    {
//      System.out.println("    factor = " + factor);
      sum += factor;
    }
    return sum;
  }

  public static void main(String[] args)
  {
    for (long i = 1; i < LIMIT; i++)
    {
      if (amicableNumbers.contains(i))
      {
        continue;
      }

//      System.out.println("i = " + i);
      long sumOfFactors = sumOfFactors(i);
      if (sumOfFactors == 0)
      {
        continue;
      }

      long sumOfSumOfFactors = sumOfFactors(sumOfFactors);
      if (i == sumOfSumOfFactors && sumOfFactors != sumOfSumOfFactors)
      {
        System.out.println("i/sumOfFactors = " + i + "/" + sumOfFactors);
        amicableNumbers.add(i);
        amicableNumbers.add(sumOfFactors);
      }
    }

    long sum = 0;
    for (Long amicableNumber : amicableNumbers)
    {
      sum += amicableNumber;
    }
    System.out.println("sum = " + sum);

    Set<Long> zz = getFactors(220);
    for (Long aLong : zz)
    {
      System.out.println("  zz = " + aLong);
    }
  }

}
