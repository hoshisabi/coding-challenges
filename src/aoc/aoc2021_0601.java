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
import java.util.stream.Collectors;

public class aoc2021_0601
{
  public static class LanternFish
  {
    List<Integer> lanternFishState;

    public LanternFish(String initials)
    {
      lanternFishState = Arrays.stream(initials.split(",")).map(Integer::parseInt).collect(Collectors.toList());
    }

    public int advance()
    {
      List<Integer> newGeneration = new ArrayList<>();
      int births = 0;
      for (Integer lanternFish : lanternFishState)
      {
        if (lanternFish == 0)
        {
          newGeneration.add(6);
          births++;
        }
        else
        {
          newGeneration.add(lanternFish - 1);
        }
      }

      for (int i = 0; i < births; i++)
      {
        newGeneration.add(8);
      }

      lanternFishState = newGeneration;
      return newGeneration.size();
    }

    public int advance(int i)
    {
//      System.out.println("Initial = " + lanternFishState);
      for (int j = 0; j < i; j++)
      {
        advance();
//        System.out.println("After " + (j + 1) + " days = " + lanternFishState);
      }
      return lanternFishState.size();
    }
  }

  public aoc2021_0601(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);

    LanternFish lf = new LanternFish(strings.get(0));
    System.out.println("lf.advance(80) = " + lf.advance(80));
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0601 me = new aoc2021_0601("aoc2021_0601_testinput.txt");
      aoc2021_0601 me = new aoc2021_0601("aoc2021_0601_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
