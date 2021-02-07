package pe;

import java.math.*;

public class PE16
{

  public static void main(String[] args)
  {
    long sum = 0;
    BigInteger number = new BigInteger("1");
    String numberStr = number.shiftLeft(1000).toString();
    for (int i = 0; i < numberStr.length(); i++)
    {
      int digit =  numberStr.charAt(i) - '0';
      System.out.println("digit = " + digit);
      sum += digit;
    }
    System.out.println("sum = " + sum);
  }
}
