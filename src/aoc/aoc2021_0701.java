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

public class aoc2021_0701
{
  public class CrabFleet
  {
    List<Integer> crabSubs;

    public CrabFleet(List<Integer> positions)
    {
      crabSubs = positions;
    }

    public int recalibrateToPos(int i)
    {
      int fuelCost = 0;

      for (Integer crabSub : crabSubs)
      {
        fuelCost += Math.abs(crabSub - i);
      }
      System.out.println("recalibrating to " + i + " costs " + fuelCost);

      return fuelCost;
    }

    public int recalibrateToMinPos()
    {
      int minSub = Collections.min(crabSubs);
      int maxSub = Collections.max(crabSubs);
      int minFuelCost = Integer.MAX_VALUE;

      for (int i = minSub; i <= maxSub; i++)
      {
        minFuelCost = Math.min(recalibrateToPos(i), minFuelCost);
      }

      return minFuelCost;
    }

    @Override
    public String toString()
    {
      return "CrabFleet{" +
          "crabSub=" + crabSubs +
          '}';
    }
  }


  public aoc2021_0701(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);
    String[] splitFirstString = strings.get(0).split(",");
    List<Integer> intList = Arrays.stream(splitFirstString).map(Integer::parseInt).collect(Collectors.toList());
    CrabFleet fleet = new CrabFleet(intList);
    System.out.println("fleet = " + fleet);
    int fuel = fleet.recalibrateToMinPos();
    System.out.println("fuel = " + fuel);;
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0701 me = new aoc2021_0701("aoc2021_0701_testinput.txt");
      aoc2021_0701 me = new aoc2021_0701("aoc2021_0701_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
