package pe;

import java.util.*;

public class PE31_alt
{

  int validCurrencies[] = {200, 100, 50, 20, 10, 5, 2, 1};

  List<Map<Integer, Integer>> validChange = new ArrayList<Map<Integer, Integer>>();

  private static String convertMapToString(Map<Integer, Integer> oneSetOfChange)
  {
    StringBuilder changeStr = new StringBuilder();

    for (Integer coin : oneSetOfChange.keySet())
    {
      if (changeStr.length() > 0)
      {
        changeStr.append(", ");
      }
      changeStr.append(coin);
      if (oneSetOfChange.get(coin) > 1)
      {
        changeStr.append("x").append(oneSetOfChange.get(coin));
      }

    }

    return changeStr.toString();

  }

  /**
   * @param args
   */
  public static void main(String[] args)
  {


  }

}
