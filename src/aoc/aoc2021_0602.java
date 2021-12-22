package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class aoc2021_0602
{
  public static class LanternFish
  {
    long[] lanternFishState = new long[9];

    public LanternFish(String initials)
    {
      for (int i = 0; i < 9; i++)
      {
        lanternFishState[i] = 0;
      }

      for (String entry : initials.split(","))
      {
        lanternFishState[Integer.parseInt(entry)]++;
      }
    }

    public long advance()
    {
      long[] newLanternFishState = new long[9];

      // Skip 0s for now.

      for (int i = 1; i < 9; i++)
      {
        newLanternFishState[i-1] = lanternFishState[i];
      }

      newLanternFishState[6] += lanternFishState[0];
      newLanternFishState[8] += lanternFishState[0];


      lanternFishState = newLanternFishState;
      displayState();
      return sum();
    }

    public void displayState()
    {
      for (int i = 0; i < 9; i++)
      {
        System.out.println("  Gen " + i + ": " + lanternFishState[i]);
      }
    }

    public long advance(int i)
    {
      System.out.println("Initial = " + sum());
      for (int j = 0; j < i; j++)
      {
        System.out.println("After " + (j + 1) + " days = " + advance());
      }
      return sum();
    }

    public long sum()
    {
      return Arrays.stream(lanternFishState).sum();
    }
  }

  public aoc2021_0602(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);

    LanternFish lf = new LanternFish(strings.get(0));
    lf.displayState();

    System.out.println("lf.advance(256) = " + lf.advance(256));
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0602 me = new aoc2021_0602("aoc2021_0601_testinput.txt");
      aoc2021_0602 me = new aoc2021_0602("aoc2021_0601_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
