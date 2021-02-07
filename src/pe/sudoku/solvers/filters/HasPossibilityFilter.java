package pe.sudoku.solvers.filters;

import pe.sudoku.*;

public class HasPossibilityFilter implements CellFilter
{
  private int value;

  public HasPossibilityFilter(int value)
  {
    this.value = value;
  }

  public boolean accept(Cell c)
  {
    return c.hasPossibility(value);
  }
}
