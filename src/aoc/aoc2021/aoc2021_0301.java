package aoc2021;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class aoc2021_0301
{
  public static List<String> readFileStrings(String filename) throws IOException, URISyntaxException {
    return Files.readAllLines(Paths.get(aoc2021_0301.class.getResource(filename).toURI()), Charset.defaultCharset())
            .stream()
            .toList();
  }


  public static void incrCountMap(Map<Integer, Integer> countMap, int i)
  {
    Integer newCount = countMap.get(i);
    if (newCount == null)
    {
      newCount = 0;
    }
    newCount++;
    countMap.put(i, newCount);
  }

  public static int getGamma(Map<Integer, Integer> oneCountMap, Map<Integer, Integer> zeroCountMap, int wordSize)
  {
    int gamma = 0;
    String binaryString = "";
    for (int i = 0; i < wordSize; i++)
    {
      Integer ones = oneCountMap.get(wordSize - 1 - i);
      Integer zeros = zeroCountMap.get(wordSize - 1 - i);
      if (ones > zeros)
      {
        int mask = 1 << i;
        gamma |= mask;
        binaryString = "1" + binaryString;
      }
      else
      {
        binaryString = "0" + binaryString;
      }
    }
    System.out.println("binaryString = " + binaryString);
    return gamma;
  }

  public static int getEpsilon(int gamma, int wordSize)
  {
    int mask = (1 << wordSize) - 1;
    return mask ^ gamma;
  }

  public static int mcb(List<String> arr)
  {
    int wordSize = arr.get(0).length();

    Map<Integer, Integer> oneCount = new HashMap(wordSize);
    Map<Integer, Integer> zeroCount = new HashMap(wordSize);
    for (String item : arr)
    {
      System.out.println("item = " + item);
      for (int i = 0; i < wordSize; i++)
      {
        String oneChar = item.substring(i, i + 1);
        System.out.println(oneChar);
        if (oneChar.equals("0"))
        {
          incrCountMap(zeroCount, i);
        }
        else
        {
          incrCountMap(oneCount, i);
        }
      }
    }
    System.out.println("zeroCount = " + zeroCount);
    System.out.println("oneCount = " + oneCount);

    int gamma = getGamma(oneCount, zeroCount, wordSize);
    int epsilon = getEpsilon(gamma, wordSize);
    System.out.println(gamma);
    System.out.println(epsilon);
    System.out.println("Multiplied: " + gamma * epsilon);

    return 0;
  }


  public static void main(String[] arr)
  {
      List<String> inputData = null;
      try {
          inputData = AocUtil.readLines("aoc-input/aoc2021_0301_input.txt");
      } catch (Exception e) {
          e.printStackTrace();
      }
      System.out.println("mcb(new int[]{}) = " + mcb(inputData));
  }
}

