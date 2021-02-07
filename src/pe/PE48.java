package pe;

import java.math.*;

public class PE48
{
  private static final int LIMIT = 1000;

  public static void main(String[] args)
  {
    BigDecimal sum = new BigDecimal("0");
    for (int i = 1; i <= LIMIT; i++)
    {
      sum = sum.add(new BigDecimal(i).pow(i));
    }
    String sumStr = sum.toString();
    sumStr = sumStr.substring(sumStr.length() - 10);
    System.out.println("sum = " +sumStr);
  }
}
