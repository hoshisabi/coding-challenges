
package pe.sudoku;

import java.util.*;
import java.io.*;

import pe.sudoku.solvers.*;

public class App
{
  private Puzzle puzzle = null;
  private static final List<PuzzleSolver> solverList = new ArrayList<PuzzleSolver>(Arrays.asList(
    new ConstantSolver(),
    new OnlyPossibilitySolver()
  ));

  public Puzzle getPuzzle()
  {
    return puzzle;
  }

  public App(String[] puzzleStrings)
  {
    puzzle = getPuzzle(puzzleStrings);
    puzzle.setChanged(true);


    while (puzzle.isChanged())
    {
      puzzle = runSolvers(puzzle, solverList);
    }
  }

  public Puzzle getPuzzle(String[] input)
  {
    Puzzle puzzle = new Puzzle(input[0]);

    for (int outIdx = 1; outIdx < input.length; outIdx++)
    {
      String line = input[outIdx];
      for (int inIdx = 0; inIdx < line.length(); inIdx++)
      {
        puzzle.setCellFromString(inIdx, outIdx - 1, line.substring(inIdx, inIdx + 1));
      }
    }

    return puzzle;
  }

  public Puzzle runSolvers(Puzzle puzzle, List<PuzzleSolver> solvers)
  {
    Puzzle modifiedPuzzle = new Puzzle(puzzle);
    modifiedPuzzle.setChanged(false);

    for (PuzzleSolver solver : solvers)
    {
      modifiedPuzzle = solver.solvePuzzle(modifiedPuzzle);
    }
    modifiedPuzzle.setChanged(!modifiedPuzzle.sameBoard(puzzle));

    return modifiedPuzzle;
  }

  public static void main(String[] args)
  {
    File puzzleFile = new File("C:\\Documents and Settings\\dchapman\\Desktop\\Sunday\\PE\\src\\pe\\sudoku\\PE96.txt");

    try
    {
//      App me = new App(new String[]{
//        "Grid 01",
//        "003020600",
//        "900305001",
//        "001806400",
//        "008102900",
//        "700000008",
//        "006708200",
//        "002609500",
//        "800203009",
//        "005010300",
//      });
//      App me = new App(new String[]{
//        "Grid 02",
//        "200080300",
//        "060070084",
//        "030500209",
//        "000105408",
//        "000000000",
//        "402706000",
//        "301007040",
//        "720040060",
//        "004010003",
//      });
      App me = new App(new String[]{
        "Grid 03",
        "000000907",
        "000420180",
        "000705026",
        "100904000",
        "050000040",
        "000507009",
        "920108000",
        "034059000",
        "507000000",
      });

      Puzzle puz = me.getPuzzle();
      System.out.println(puz);
      if (!puz.isSolved())
      {
        System.out.println("Could not solve puzzle " + puz.getName());
        System.exit(-1);
      }
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
