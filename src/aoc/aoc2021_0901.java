package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class aoc2021_0901
{
  public static class Coord
  {
    int x;
    int y;

    public Coord(int x, int y)
    {
      this.x = x;
      this.y = y;
    }

    @Override
    public String toString()
    {
      return "Coord{" +
          "x=" + x +
          ", y=" + y +
          '}';
    }

    @Override
    public boolean equals(Object o)
    {
      if (this == o)
      {
        return true;
      }
      if (o == null || getClass() != o.getClass())
      {
        return false;
      }
      Coord coord = (Coord) o;
      return x == coord.x && y == coord.y;
    }

    @Override
    public int hashCode()
    {
      return Objects.hash(x, y);
    }
  }

  public class HeightMap
  {
    Map<Coord, Integer> readings;
    int maxX;
    int maxY;

    public HeightMap(List<String> lines)
    {

      readings = new HashMap<>();
      for (int y = 0; y < lines.size(); y++)
      {
        String[] line = lines.get(y).split("");
        for (int x = 0; x < line.length; x++)
        {
          Coord c = new Coord(x, y);
          readings.put(c, Integer.parseInt(line[x]));
        }

        maxY = lines.size() - 1;
        maxX = line.length - 1;
      }
    }

    public List<Coord> getNeighbors(Coord c)
    {
      List<Coord> neighbors = new ArrayList<>();
      if (c.x > 0)
      {
        neighbors.add(new Coord(c.x - 1, c.y));
      }
      if (c.x < maxX)
      {
        neighbors.add(new Coord(c.x + 1, c.y));
      }
      if (c.y > 0)
      {
        neighbors.add(new Coord(c.x, c.y - 1));
      }
      if (c.y < maxY)
      {
        neighbors.add(new Coord(c.x, c.y + 1));
      }
      return neighbors;
    }

    public List<Coord> findLowPoints()
    {
      List<Coord> lowPoints = new ArrayList<>();
      for (Coord coord : readings.keySet())
      {
        boolean lowPoint = true;
        int reading = getHeight(coord);

        List<Coord> neighbors = getNeighbors(coord);
        for (Coord neighbor : neighbors)
        {
          if (lowPoint)
          {
            int neighborReading = getHeight(neighbor);
            if (reading >= neighborReading)
            {
              lowPoint = false;
              break;
            }
          }
        }
        if (lowPoint)
        {
          lowPoints.add(coord);
        }
      }

      return lowPoints;
    }

    private Integer getHeight(Coord coord)
    {
      if (!readings.containsKey(coord))
      {
        System.out.println("missing coord = " + coord);
      }
      return readings.get(coord);
    }

    @Override
    public String toString()
    {
      return "HeightMap{" +
          "maxX=" + maxX +
          ", maxY=" + maxY +
          ", readings=" + readings +
          '}';
    }
  }

  public aoc2021_0901(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    HeightMap hm = new HeightMap(strings);
    System.out.println("hm = " + hm);

    int sum = 0;
    List<Coord> lowPoints = hm.findLowPoints();
    for (Coord lowPoint : lowPoints)
    {
      Integer riskLevel = hm.getHeight(lowPoint) + 1;
      System.out.println("lowPoint = " + lowPoint + ", Reading = " + riskLevel);
      sum += riskLevel;
    }
    System.out.println("sum = " + sum);
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0901 me = new aoc2021_0901("aoc2021_0901_testinput.txt");
      aoc2021_0901 me = new aoc2021_0901("aoc2021_0901_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
