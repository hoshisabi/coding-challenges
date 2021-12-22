package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class aoc2021_0501
{
  public static class Point
  {
    int x;
    int y;

    public Point(int x, int y)
    {
      this.x = x;
      this.y = y;
    }

    public int getX()
    {
      return x;
    }

    public int getY()
    {
      return y;
    }

    @Override
    public String toString()
    {
      return "Point{" +
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
      Point point = (Point) o;
      return x == point.x && y == point.y;
    }

    @Override
    public int hashCode()
    {
      return Objects.hash(x, y);
    }
  }

  public static class Grid
  {
    Map<Point, Integer> countMap;

    public Grid()
    {
      this.countMap = new HashMap<>();
    }

    public void plotLine(int x1, int y1, int x2, int y2)
    {
      int diffX = Math.abs(x1 - x2);
      int diffY = Math.abs(y1 - y2);
      int maxDiff = Math.max(diffX, diffY);

      if (diffX != 0 && diffY != 0 && diffX != diffY)
      {
        System.out.println("Invalid line: " + x1 + "," + y1 + "->" + x2 + "," + y2 +
            " diffX=" + diffX + ", diffY=" +diffY);
      }


      for (int i = 0; i <= maxDiff; i++)
      {
        int x = -1;
        if (x1 == x2)
        {
          x = x1;
        }
        else if (x1 > x2)
        {
          x = x1 - i;
        }
        else
        {
          x = x1 + i;
        }
        int y = -1;
        if (y1 == y2)
        {
          y = y1;
        }
        else if (y1 > y2)
        {
          y = y1 - i;
        }
        else
        {
          y = y1 + i;
        }

        plotPoint(x, y);
      }
    }

    private void plotPoint(int x, int y)
    {
      Point key = new Point(x, y);
      Integer count = countMap.get(key);
      if (count == null)
      {
        count = 0;
      }
      System.out.println("Putting: x=" + x + ",y=" + y);
      countMap.put(key, ++count);
    }

    public int getIntersectionCount()
    {
      int sum = 0;
      for (Integer value : countMap.values())
      {
        if (value > 1)
        {
          sum++;
        }
      }
      return sum;
    }
  }

  public aoc2021_0501(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);

    Grid grid = new Grid();

    for (String line : strings)
    {
      String[] coords = line.split("[-,> ]+");
      System.out.println(line);
      System.out.println(Arrays.asList(coords));
      grid.plotLine(Integer.parseInt(coords[0]), Integer.parseInt(coords[1]),
          Integer.parseInt(coords[2]), Integer.parseInt(coords[3]));
    }


    System.out.println("Intersection count: " + grid.getIntersectionCount());

  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0501 me = new aoc2021_0501("aoc2021_0501_testinput.txt");
      aoc2021_0501 me = new aoc2021_0501("aoc2021_0501_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
