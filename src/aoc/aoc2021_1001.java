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
  public enum BracketType
  {
    ROUND("(", ")", 3, 1),
    SQUARE("[", "]", 57, 2),
    CURLY("{", "}", 1197, 3),
    ANGLE("<", ">", 25137, 4);

    private final String closeBracket;
    private final String openBracket;
    private final int corruptionScore;
    private final int incompleteScore;

    BracketType(String openBracket, String closeBracket, int corruptionScore, int incompleteScore)
    {
      this.openBracket = openBracket;
      this.closeBracket = closeBracket;
      this.corruptionScore = corruptionScore;
      this.incompleteScore = incompleteScore;
    }

    public String getCloseBracket()
    {
      return closeBracket;
    }

    public String getOpenBracket()
    {
      return openBracket;
    }

    public int getCorruption()
    {
      return corruptionScore;
    }

    public int getIncompleteScore()
    {
      return incompleteScore;
    }

    public static BracketType getBracketType(String c)
    {
      for (BracketType value : values())
      {
        if (value.closeBracket.equals(c) || value.openBracket.equals(c))
        {
          return value;
        }
      }
      return null;
    }

    public static boolean isOpenBracket(String c)
    {
      for (BracketType value : values())
      {
        if (value.openBracket.equals(c))
        {
          return true;
        }
      }
      return false;
    }
  }

  public aoc2021_1001(String filename) throws IOException, URISyntaxException
  {
    Deque<BracketType> bracketStack = new ArrayDeque<>();
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    int lineNumber = 0;
    int totalCorruption = 0;
    List<Long> incompleteScores = new ArrayList<>();
    for (String line : lines)
    {
      bracketStack.clear();
      lineNumber++;
      String[] characters = line.split("");
      for (String character : characters)
      {
        BracketType bracket = BracketType.getBracketType(character);
        if (BracketType.isOpenBracket(character))
        {
          bracketStack.push(bracket);
        }
        else if (bracket != null)
        {
          if (bracket != bracketStack.pop())
          {
            totalCorruption += bracket.getCorruption();
            System.out.println("Corrupt Line #" + lineNumber + ": corrupt score=" + bracket.getCorruption() + ", corrupt total so far=" + totalCorruption);
            bracketStack.clear();
            break;
          }
        }
      }
      if (bracketStack.size() > 0)
      {
        long incompleteScore = 0;
        for (BracketType bracket : bracketStack)
        {
          incompleteScore *= 5;
          incompleteScore += bracket.incompleteScore;
        }

        System.out.println("Incomplete Line #" + lineNumber + ": incomplete score=" + incompleteScore);
        incompleteScores.add(incompleteScore);
      }
    }
    incompleteScores.sort(Long::compareTo);
    int mid = incompleteScores.size() / 2;
    System.out.println("incompleteScores = " + incompleteScores.get(mid));
    System.out.println("totalCorruptScore = " + totalCorruption);
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_1001 me = new aoc2021_1001("aoc2021_1001_testinput.txt");
      aoc2021_1001 me = new aoc2021_1001("aoc2021_1001_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
