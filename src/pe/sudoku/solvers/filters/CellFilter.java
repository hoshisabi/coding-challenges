package pe.sudoku.solvers.filters;

import pe.sudoku.*;

public interface CellFilter
{
  public boolean accept(Cell c);
}
