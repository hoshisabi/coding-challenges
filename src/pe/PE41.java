package pe;

import java.util.*;

public class PE41
{
  static List<Long> generateListWithDigits(long baseNum, int digit)
  {
    String baseStr = Long.toString(baseNum);
    List<Long> retList = new ArrayList<Long>();
    for (int i = 0; i <= baseStr.length(); i++)
    {
      String numberStr = baseStr.substring(0, i) + digit + baseStr.substring(i);
      retList.add(Long.parseLong(numberStr));
    }
    return retList;
  }

  static List<Long> generatePandigitalDigits()
  {
    List<Long> retList = new ArrayList<Long>();
    retList.add(1L);
    List<Long> lastList = retList;
    for (int i = 2; i < 9; i++)
    {
      List<Long> subList = new ArrayList<Long>();
      for (Long oneNumber : lastList)
      {
        subList.addAll(generateListWithDigits(oneNumber, i));
      }
      retList.addAll(subList);
      lastList = subList;
    }
    return retList;
  }

  public static void main(String[] args)
  {
    List<Long> nums = generatePandigitalDigits();
    Collections.sort(nums, Collections.reverseOrder());
    for (Long num : nums)
    {
      if (PEUtil.isPrime(num))
      {
        System.out.println("prime num = " + num);
        break;
      }
      else                        {
        System.out.println("num not prime= " + num);
      }
    }
  }
}
