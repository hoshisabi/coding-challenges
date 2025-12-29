package aoc_2021;

import aoc_shared.DataLoader;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class aoc2021_0801
{
  public aoc2021_0801(List<String> strings )
  {
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
    List<String> lines = DataLoader.loadInput(2021, 8, 1, false);
    aoc2021_0801 me = new aoc2021_0801(lines);
  }
}
