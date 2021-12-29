package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class aoc2021_0101
{
  public static int countLarger(List<Integer> depths)
  {
    int largerCount = 0;
    Integer lastCount = depths.get(0);
    for (Integer depth : depths)
    {
      if (lastCount < depth)
      {
        largerCount++;
      }
      lastCount = depth;
    }
    return largerCount;
  }

  public static List<Integer> readFile(String filename) throws IOException, URISyntaxException
  {
    URI uri = aoc2021_0101.class.getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    List<Integer> valueList = strings.stream().map(l -> Integer.valueOf(l)).collect(Collectors.toList());
    return valueList;
  }


  public static void main(String[] args)
  {
    try
    {
      List<Integer> integers = aoc2021_0101.readFile("aoc2021_0101_input.txt");
      int countLarger = aoc2021_0101.countLarger(integers);
      System.out.println("countLarger = " + countLarger);
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
