package pe;

import java.util.*;
import java.math.BigInteger;

public class PE20
{

  private static void addDigitToList(List<Integer> digitList, int digit)
  {
    if (digit == 1 || digit == 0)
    {
      // do nothing
    }
    else if (digit % 10 == 0)
    {
      addDigitToList(digitList, digit / 10);
    }
    else if (digit == 2)
    {
      // If we have a 5 in the list, we can remove it now, since with this 2 it adds up to 10
      if (digitList.contains(5))
      {
        digitList.remove(digitList.
          indexOf(5));
      }
      // Well, guess not, we just add it to the list
      else
      {
        digitList.add(2);
      }
    }
    else if (digit == 5)
    {
      // If we have a 2 in the list, we can remove it now, since with this 5 it adds up to 10
      if (digitList.contains(2))
      {
        digitList.remove(digitList.indexOf(2));
      }
      // Well, guess not, we just add it to the list
      else
      {
        digitList.add(5);
      }
    }
    else if (digit % 2 == 0)
    {
      addDigitToList(digitList, 2);
      addDigitToList(digitList, digit / 2);
    }
    else if (digit % 5 == 0)
    {
      addDigitToList(digitList, 5);
      addDigitToList(digitList, digit / 5);
    }
    else if (digit != 7 && digit % 7 == 0)
    {
      addDigitToList(digitList, 7);
      addDigitToList(digitList, digit / 7);
    }
    else if (digit != 3 && digit % 3 == 0)
    {
      addDigitToList(digitList, 3);
      addDigitToList(digitList, digit / 3);
    }
    else if (digit != 11 && digit % 11 == 0)
    {
      addDigitToList(digitList, 11);
      addDigitToList(digitList, digit / 11);
    }
    else
    {
      digitList.add(digit);
    }
  }

  public static void main(String[] args)
  {
    List<Integer> copyIntegerList = new ArrayList<Integer>();
    for (int i = 1; i <= 100; i++)
    {
      // the add digit to list function turns out to not be a savings at all,
      // since I couldn't figure out enough ways to eliminate digits to actual
      // spare us from having to use a big integer
      // addDigitToList(copyIntegerList, i);
      copyIntegerList.add(i);
    }

//    Collections.sort(copyIntegerList);
//    for (Integer integer : copyIntegerList)
//    {
//      System.out.println("integer = " + integer);
//    }
//    System.out.println("copyIntegerList.size() = " + copyIntegerList.size());

    int sumOfDigits = getProductOfList(copyIntegerList);
    System.out.println("correct = " + (sumOfDigits == 648));

  }

  private static int getProductOfList(Collection<Integer> copyIntegerList)
  {
    BigInteger product = BigInteger.ONE;
    for (Integer integer : copyIntegerList)
    {
      product = product.multiply(new BigInteger(integer.toString()));
    }
    System.out.println("product = " + product + "\nsize of product=" + product.toString().length());

    int sumOfDigits = 0;
    while (product.compareTo(BigInteger.TEN) == 1)
    {
      BigInteger[] bigIntegers = product.divideAndRemainder(BigInteger.TEN);
      product = bigIntegers[0];
      sumOfDigits += bigIntegers[1].intValue();
    }

    sumOfDigits += product.intValue();
    System.out.println("sumOfDigits = " + sumOfDigits);
    return sumOfDigits;
  }
} 