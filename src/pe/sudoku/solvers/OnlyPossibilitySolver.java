
package pe.sudoku.solvers;

import java.util.*;

import pe.sudoku.*;

public class OnlyPossibilitySolver implements PuzzleSolver
{
  public Puzzle solvePuzzle(Puzzle puzzle)
  {
    Puzzle modifiedPuzzle = new Puzzle(puzzle);

    for (int s = 0; s < Puzzle.BOARD_SIZE; s++)
    {
      for (int v = 0; v < Puzzle.BOARD_SIZE; v++)
      {
        setIfOnlyValueInList(modifiedPuzzle.getRow(s), v);
        setIfOnlyValueInList(modifiedPuzzle.getColumn(s), v);
        setIfOnlyValueInList(modifiedPuzzle.getQuadrant(s), v);
      }
    }

    return modifiedPuzzle;
  }

  private void setIfOnlyValueInList(List<Cell> cells, int v)
  {
    Cell whichCell = null;
    int numPoss = 0;

    for (Cell cell : cells)
    {
      if (cell.getValue() == v)
      {
        return;
      }

      if (cell.hasPossibility(v))
      {
        numPoss++;
        whichCell = cell;
      }
    }

    // If one, and only one, cell has this value, then we can set it
    // as the only possibility
    if (numPoss == 1)
    {
      whichCell.setValue(v);
    }

  }
}
