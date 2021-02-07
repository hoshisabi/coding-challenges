
package pe.sudoku;

import java.util.*;

public class Cell
{
  int x = 0;
  int y = 0;
  int q = 0;

  private Set<Integer> possibilities = new HashSet<Integer>();

  public Cell(Set<Integer> possibilities)
  {
    this.possibilities = new HashSet<Integer>(possibilities);
  }

  /**
   * Remove this value as a possible (pencil-mark) value
   *
   * @param value
   */
  public void removePossibility(int value)
  {
    possibilities.remove(value);
  }

  /**
   * Set this value as a definite value
   *
   * @param value
   */
  public void setValue(int value)
  {
    possibilities = new HashSet<Integer>(Arrays.asList(value));
  }

  /**
   * If there is only one possible value, return the value, otherwise return -1
   *
   * @return
   */
  public int getValue()
  {
    if (possibilities.size() != 1)
    {
      return -1;
    }
    else
    {
      return possibilities.iterator().next();
    }
  }

  /**
   * Get the set of possibilities that this cell allows.
   *
   * @return
   */
  public Set<Integer> getPossibilities()
  {
    return new HashSet<Integer>(possibilities);
  }

  public boolean hasPossibility(int value)
  {
    return possibilities.contains(value);
  }

  @Override
  public String toString()
  {
    if (possibilities.size() > 1)
    {
      return "0";
    }
    else
    {
      return Integer.toString(possibilities.iterator().next());
    }
  }

  public boolean sameCell(Cell cellAt)
  {
    return possibilities.size() == cellAt.getPossibilities().size();
  }

  public int getX()
  {
    return x;
  }

  public void setX(int x)
  {
    this.x = x;
  }

  public int getY()
  {
    return y;
  }

  public void setY(int y)
  {
    this.y = y;
  }

  public int getQ()
  {
    return q;
  }

  public void setQ(int q)
  {
    this.q = q;
  }
}
