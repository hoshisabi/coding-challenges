
package pe.sudoku.solvers;

import java.util.*;

import pe.sudoku.*;

public class ConstantSolver implements PuzzleSolver
{
  public Puzzle solvePuzzle(Puzzle puzzle)
  {
    Puzzle modifiedPuzzle = new Puzzle(puzzle);

    for (int x = 0; x < Puzzle.BOARD_SIZE; x++)
    {
      for (int y = 0; y < Puzzle.BOARD_SIZE; y++)
      {
        Cell cell = puzzle.getCellAt(x, y);
        int value = cell.getValue();
        if (value != -1)
        {
          removeFromList(modifiedPuzzle.getRow(y), value);
          removeFromList(modifiedPuzzle.getColumn(x), value);
          removeFromList(modifiedPuzzle.getQuadrant(x, y), value);
        }
      }
    }

    return modifiedPuzzle;
  }

  private void removeFromList(List<Cell> cells, int value)
  {
    for (Cell cell : cells)
    {
      // If the cell has this value, then it was what kicked
      // off the removal process, otherwise reomve it.
      // If the cell already is missing this, nothing harmed.
      if (cell.getValue() != value)
      {
        cell.removePossibility(value);
      }
    }
  }
}
