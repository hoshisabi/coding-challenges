package aoc2021;

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

public class aoc2021_0401
{
  public void runWithFile(String filename) throws URISyntaxException, IOException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    BingoGame game = new BingoGame(strings);
    System.out.println(game.picks);

    List<BingoBoard> boards = game.getBoards();

    boolean won = false;
    for (Integer pick : game.picks)
    {
      System.out.println("==============");
      System.out.println("Now using pick: " + pick);
      for (BingoBoard board : boards)
      {
        if (board.isWon())
          continue;

        board.markValue(pick);
        board.printBoard();
        if (board.isWon())
        {
          won = true;
          System.out.println("Won?" + board.isWon() + " Sum: " + board.getSum() + " Score: " + board.getSum() * pick);
        }
      }
    }
  }

  public class BingoGame
  {
    public List<Integer> picks;
    public List<BingoBoard> boards;

    public BingoGame(List<String> fileInput)
    {
      String firstLine = fileInput.remove(0);
      picks = Arrays.stream(firstLine.split(",")).
          map(x -> Integer.parseInt(x)).collect(Collectors.toList());
      boards = new ArrayList<>();

      while (true)
      {
        if (fileInput.isEmpty())
        {
          break;
        }

        String[] boardInput = new String[5];
        for (int i = 0; i < 5; i++)
        {
          String line = fileInput.remove(0);
          if (line == null || line.trim().isEmpty())
          {
            line = fileInput.remove(0);
          }
          boardInput[i] = line;
        }
        BingoBoard board = new BingoBoard(boardInput);
        boards.add(board);
      }
    }

    public List<Integer> getPicks()
    {
      return picks;
    }

    public List<BingoBoard> getBoards()
    {
      return boards;
    }
  }

  public class BingoBoard
  {
    int[][] boardValues = new int[5][5];

    public BingoBoard(String[] boardInput)
    {
      for (int x = 0; x < 5; x++)
      {
        String line = boardInput[x];
        String[] rowArr = line.trim().split("\\s+");
        for (int y = 0; y < 5; y++)
        {
          boardValues[x][y] = Integer.parseInt(rowArr[y]);
        }
      }
    }

    public void markValue(int i)
    {
      for (int x = 0; x < 5; x++)
      {
        for (int y = 0; y < 5; y++)
        {
          if (boardValues[x][y] == i)
          {
            boardValues[x][y] = -1;
          }
        }
      }
    }

    public boolean isWon()
    {
      int diaUpSum = 0;
      int diaDownSum = 0;

      for (int x = 0; x < 5; x++)
      {
        diaDownSum += boardValues[x][x];
        diaUpSum += boardValues[4 - x][4 - x];

        int rowSum = 0;
        int colSum = 0;

        for (int y = 0; y < 5; y++)
        {
          rowSum += boardValues[x][y];
          colSum += boardValues[y][x];
        }

        if (rowSum == -5)
        {
          return true;
        }
        if (colSum == -5)
        {
          return true;
        }
      }

      return diaUpSum == 0 || diaDownSum == 0;
    }

    public int getSum()
    {
      int sum = 0;
      for (int x = 0; x < 5; x++)
      {
        for (int y = 0; y < 5; y++)
        {
          int cellVal = boardValues[x][y];
          if (cellVal != -1)
          {
            sum += cellVal;
          }
        }
      }
      return sum;
    }

    void printBoard()
    {
      for (int[] boardValue : boardValues)
      {
        for (int i : boardValue)
        {
          System.out.print(i + "\t");
        }
        System.out.println();
      }
    }
  }

  public static void main(String[] args)
  {
    aoc2021_0401 me = new aoc2021_0401();
    try
    {
//      me.runWithFile("aoc2021_0401_testinput.txt");
      me.runWithFile("aoc2021_0401_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
