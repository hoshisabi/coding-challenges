
package pe.sudoku.solvers;

import pe.sudoku.*;

public class ConstrainedChoiceSolver
{
  public Puzzle solvePuzzle(Puzzle puzzle)
  {
    Puzzle modifiedPuzzle = new Puzzle(puzzle);

    for (int s = 0; s < Puzzle.BOARD_SIZE; s++)
    {
      for (int v = 0; v < Puzzle.BOARD_SIZE; v++)
      {
//        fixConstrainedValue(modifiedPuzzle.getRow(s), modifiedPuzzle.getQuadrant(s))
      }
    }

    return modifiedPuzzle;
  }


}
