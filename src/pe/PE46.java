package pe;

import java.util.*;

public class PE46
{
  private static Map<Integer, Boolean> primesCheck = new HashMap<Integer, Boolean>();

  static boolean isPrime(int number)
  {
    if (number <= 0)
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

  public static void main(String[] args)
  {
    int number = 7;

    outer:
    while (true)
    {
      number += 2;
      if (!isPrime(number))
      {
        for (int i = number; i > 0; i--)
        {
          int primeCheck = number - 2 * i * i;
          if (isPrime(primeCheck))
          {
            System.out.println(number + " = " + primeCheck + " + 2 * " + i + "^2");
            continue outer;
          }
        }
        System.out.println("Correct number = " + number);
        break;
      }
    }
  }

}
