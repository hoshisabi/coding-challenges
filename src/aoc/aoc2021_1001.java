package aoc;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;

public class aoc2021_1001
{

  public aoc2021_1001(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
  }

  public static void main(String[] args)
  {
    try
    {
      aoc2021_1001 me = new aoc2021_1001("aoc2021_1001_testinput.txt");
//      aoc2021_1001 me = new aoc2021_1001("aoc2021_1001_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
