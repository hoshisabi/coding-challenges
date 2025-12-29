package aoc_2021;

import aoc_shared.DataLoader;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class aoc2021_0302
{

  private static Map<Boolean, List<String>> divideCountMap(List<String> inputList, int index)
  {
    Map<Boolean, List<String>> countMap = new HashMap<>();
    countMap.put(true, new ArrayList<>());
    countMap.put(false, new ArrayList<>());

    for (String item : inputList)
    {
      if (item.charAt(index) == '0')
      {
        countMap.get(false).add(item);
      }
      else
      {
        countMap.get(true).add(item);
      }
    }
    return countMap;
  }

  public static List<String> getCarbonDioxide(List<String> inputList, int index)
  {
    Map<Boolean, List<String>> countMap = divideCountMap(inputList, index);
    System.out.println("getCarbonDioxide countMap = " + countMap + ", index=" + index);

    List<String> returnList = countMap.get(true).size() < countMap.get(false).size() ?
        countMap.get(true) : countMap.get(false);
    if (returnList.size() == 1)
    {
      return returnList;
    }
    else
    {
      return getCarbonDioxide(returnList, ++index);
    }
  }

  public static List<String> getOxygen(List<String> inputList, int index)
  {
    Map<Boolean, List<String>> countMap = divideCountMap(inputList, index);
    System.out.println("getOxygen countMap = " + countMap + ", index=" + index);

    List<String> returnList = countMap.get(true).size() >= countMap.get(false).size() ?
        countMap.get(true) : countMap.get(false);
    if (returnList.size() == 1)
    {
      return returnList;
    }
    else
    {
      return getOxygen(returnList, ++index);
    }
  }

  public static int mcb(List<String> arr)
  {
    int wordSize = arr.getFirst().length();

    String oxygenStr = getOxygen(arr, 0).getFirst();
    String carbonDioxideStr = getCarbonDioxide(arr, 0).getFirst();
    int oxygen = Integer.parseInt(oxygenStr, 2);
    int carbonDioxide = Integer.parseInt(carbonDioxideStr, 2);
    System.out.println("oxygen = " + oxygen);
    System.out.println("carbonDioxide = " + carbonDioxide);
    System.out.println("Multiplied: " + oxygen * carbonDioxide);

    return oxygen * carbonDioxide;
  }

  static void main(String[] arr)
  {
    List<String> lines = DataLoader.loadInput(2021, 3, 2, false);
    System.out.println("mcb(new int[]{}) = " + mcb(lines));
  }

}
