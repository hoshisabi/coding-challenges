package pe;

import java.util.*;

public class PE31
{

  private static List<Integer> allButHigher(List<Integer> valids, int capoff)
  {
    List<Integer> newList = new ArrayList<Integer>();
    for (Integer valid : valids)
    {
      if (valid <= capoff)
      {
        newList.add(valid);
      }
    }
    return newList;
  }

  static final List<Integer> validCurrencies = Arrays.asList(200, 100, 50, 20, 10, 5, 2, 1);

  static long countValidTypes(int remaining, List<Integer> valids)
  {
    int count = 0;

    if (remaining == 0)
    {
      count = 1;
    }
    else
    {
      for (int validCurrency : valids)
      {
        if (validCurrency <= remaining)
        {
          count += countValidTypes(remaining - validCurrency, allButHigher(validCurrencies, validCurrency));
        }
      }
    }

    return count;
  }

  /**
   * @param args
   */
  public static void main(String[] args)
  {                                        //200
    System.out.println("countVal = " + countValidTypes(200, validCurrencies));
  }
}