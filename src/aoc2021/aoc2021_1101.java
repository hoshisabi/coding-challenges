package aoc2021;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;

public class aoc2021_1101
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

  public class OctoMap
  {
    Map<Coord, Integer> readings;
    int maxX;
    int maxY;

    long flashes;

    public OctoMap(List<String> lines)
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
      flashes = 0;
    }

    public List<Coord> getNeighbors(Coord c)
    {
      List<Coord> neighbors = Arrays.asList(
          new Coord(c.x - 1, c.y - 1),
          new Coord(c.x - 1, c.y),
          new Coord(c.x - 1, c.y + 1),
          new Coord(c.x, c.y - 1),
          new Coord(c.x, c.y + 1),
          new Coord(c.x + 1, c.y - 1),
          new Coord(c.x + 1, c.y),
          new Coord(c.x + 1, c.y + 1)
      );

      return neighbors.stream().filter(f -> f.x >= 0).filter(f -> f.y >= 0).
          filter(f -> f.x <= maxX).filter(f -> f.y <= maxY).collect(Collectors.toList());
    }

    public boolean lightMap()
    {
      boolean allFlash = true;

      List<Coord> coordsToLight = new ArrayList<>();
      for (int x = 0; x <= maxX; x++)
      {
        for (int y = 0; y <= maxY; y++)
        {
          coordsToLight.add(new Coord(x, y));
        }
      }

      while (!coordsToLight.isEmpty())
      {
        Coord coord = coordsToLight.remove(0);
        Integer reading = readings.get(coord) + 1;
        readings.put(coord, reading);
        System.out.println("\tLighting " + coord + " to reading " + reading);

        if (reading == 10)
        {
          List<Coord> neighbors = getNeighbors(coord);
          System.out.println("\talso spreading to neighbors size=" + neighbors.size());
          coordsToLight.addAll(neighbors);
        }
      }

      for (Map.Entry<Coord, Integer> entry : readings.entrySet())
      {
        if (entry.getValue() > 9)
        {
          flashes++;
          readings.put(entry.getKey(), 0);
        }
        else
        {
          allFlash = false;
        }
      }
      return allFlash;
    }

    public long getFlashes()
    {
      return flashes;
    }

    @Override
    public String toString()
    {
      return "OctoMap{" +
          "maxX=" + maxX +
          ", maxY=" + maxY +
          ", flashes=" + flashes +
          ", readings=" + readings +
          '}';
    }
  }

  public aoc2021_1101(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    int lineNumber = 0;
    OctoMap octoMap = new OctoMap(lines);
    System.out.println("octoMap = " + octoMap);
    for (int i = 0; i < 1000; i++)
    {
      boolean allFlash = octoMap.lightMap();
      long l = octoMap.getFlashes();

      System.out.println("i = " + ( 1 + i) + " l = " + l + " allFlash = " + allFlash);
      if (allFlash)
      {
        break;
      }
    }
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_1101 me = new aoc2021_1101("aoc2021_1101_testinput.txt");
      aoc2021_1101 me = new aoc2021_1101("aoc2021_1101_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
