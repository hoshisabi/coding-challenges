package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class aoc2021_0801
{
  public aoc2021_0801(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);

    int sum = 0;
    for (String string : strings)
    {
      // We can throw out everything before the |
      String[] split = string.split("\\|");
      String trimLine = split[1].trim();
      String[] digits = trimLine.split("\\s");
      System.out.println(Arrays.toString(digits));
      for (String digit : digits)
      {
        int len = digit.length();
        if (len < 5 || len > 6)
        {
          System.out.println("*" + digit + "*");
          sum++;
        }
        else
        {
          System.out.println(digit);
        }
      }
    }
    System.out.println("sum = " + sum);
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0801 me = new aoc2021_0801("aoc2021_0801_testinput.txt");
      aoc2021_0801 me = new aoc2021_0801("aoc2021_0801_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
