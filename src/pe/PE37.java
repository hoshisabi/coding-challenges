package pe;

import java.util.*;

public class PE37
{
  private static Map<Integer, Boolean> primesCheck = new HashMap<Integer, Boolean>();
  private static Map<Integer, Boolean> truncatableCheck = new HashMap<Integer, Boolean>();

  static boolean isPrime(int number)
  {
    if (number <= 1)
    {
      return false;
    }

    if (!primesCheck.containsKey(number))
    {
      primesCheck.put(number, true);
      for (int i = 2; i < number; i++)
      {
        if (number % i == 0)
        {
          primesCheck.put(number, false);
          break;
        }
      }
    }

    return primesCheck.get(number);
  }

  private static boolean isTruncatable(int number)
  {
    if (!truncatableCheck.containsKey(number))
    {
      String strDigits = Integer.toString(number);

      if (!isPrime(number) || number < 10)
      {
        truncatableCheck.put(number, false);
      }
      else
      {
        boolean trunc = true;

        for (int i = 1; i < strDigits.length(); i++)
        {
          String left = strDigits.substring(0, strDigits.length() - i);
          String right = strDigits.substring(i, strDigits.length());
          if (!isPrime(Integer.parseInt(left)) || !isPrime(Integer.parseInt(right)))
          {
            trunc = false;
            break;
          }
        }
        truncatableCheck.put(number, trunc);
      }
    }

    return truncatableCheck.get(number);
  }

  public static void main(String[] args)
  {
    int number = 9;
    List<Integer> trs = new ArrayList<Integer>();

    System.out.println("isTruncatable(3797) = " + isTruncatable(3797));

    while (trs.size() < 11)
    {
      System.out.println("number = " + number);
      number += 2;
      if (number > 1000000) break;
      if (isPrime(number) && isTruncatable(number))
      {
        System.out.println("truncatable = " + number);
        trs.add(number);
      }
    }

    int sum = 0;
    for (Integer integer : trs)
    {
      sum += integer;
      System.out.println("!! integer = " + integer);
    }
    System.out.println("sum = " + sum);
  }

}
