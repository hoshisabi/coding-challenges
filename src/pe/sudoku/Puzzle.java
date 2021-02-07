package pe.sudoku;

import java.util.*;

public class Puzzle
{
  public static final int BOARD_SIZE = 9;
  private static final Set<Integer> DEFAULT_PRESET = new TreeSet<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));

  private Cell[][] board = new Cell[BOARD_SIZE][BOARD_SIZE];
  private String name = null;
  private boolean changed = false;

  public Puzzle(String name)
  {
    this.name = name;
  }

  public Puzzle(Puzzle oldPuzzle)
  {
    this.name = oldPuzzle.getName();

    for (int y = 0; y < BOARD_SIZE; y++)
    {
      for (int x = 0; x < BOARD_SIZE; x++)
      {
        createNewCellAt(x, y, oldPuzzle.getPossibilitiesAt(x, y));
      }
    }
  }


  public void setCellFromString(int x, int y, String presetVal)
  {
    if (presetVal.equals("0"))
    {
      createNewCellAt(x, y, DEFAULT_PRESET);
    }
    else
    {
      createNewCellAt(x, y, new HashSet<Integer>(Arrays.asList(Integer.parseInt(presetVal))));
    }
  }

  private void createNewCellAt(int x, int y, Set<Integer> possibilities)
  {
    Cell cell = new Cell(possibilities);
    cell.setQ(getQuadrantNumber(x, y));
    cell.setX(x);
    cell.setY(y);

    setCellAt(x, y, cell);
  }

  public String getName()
  {
    return name;
  }

  public void setName(String name)
  {
    this.name = name;
  }

  @Override
  public String toString()
  {
    StringBuilder buf = new StringBuilder(name);
    buf.append(":\n");
    for (int y = 0; y < BOARD_SIZE; y++)
    {
      for (int x = 0; x < BOARD_SIZE; x++)
      {
        buf.append(getCellAt(x, y));
      }
      buf.append("\n");
    }

    return buf.toString();
  }

  public Set<Integer> getPossibilitiesAt(int x, int y)
  {
    return getCellAt(x, y).getPossibilities();
  }

  public Cell getCellAt(int x, int y)
  {
    return board[y][x];
  }

  public void setCellAt(int x, int y, Cell cell)
  {
    board[y][x] = cell;
  }

  public List<Cell> getRow(int y)
  {
    return new ArrayList<Cell>(Arrays.asList(board[y]));
  }

  public List<Cell> getColumn(int x)
  {
    List<Cell> col = new ArrayList<Cell>();
    for (int y = 0; y < BOARD_SIZE; y++)
    {
      col.add(getCellAt(x, y));
    }

    return col;
  }

  public List<Cell> getQuadrant(int q)
  {
    List<Cell> cells = new ArrayList<Cell>();

    for (int xIdx = 0; xIdx < BOARD_SIZE; xIdx++)
    {
      for (int yIdx = 0; yIdx < BOARD_SIZE; yIdx++)
      {
        if (getQuadrantNumber(xIdx, yIdx) == q)
        {
          cells.add(getCellAt(xIdx, yIdx));
        }
      }
    }

    return cells;
  }

  public List<Cell> getQuadrant(int x, int y)
  {
    return getQuadrant(getQuadrantNumber(x, y));
  }

  public Map<Integer, List<Cell>> getQuadrantRow(int x)
  {
    Map<Integer, List<Cell>> map = new HashMap<Integer, List<Cell>>();
    for (int y = 0; y < BOARD_SIZE; y += 3)
    {
      int q = getQuadrantNumber(x, y);
      map.put(q, getQuadrant(q));
    }
    return map;
  }

  public Map<Integer, List<Cell>> getQuadrantColumn(int y)
  {
    Map<Integer, List<Cell>> map = new HashMap<Integer, List<Cell>>();
    for (int x = 0; x < BOARD_SIZE; x += 3)
    {
      int q = getQuadrantNumber(x, y);
      map.put(q, getQuadrant(q));
    }
    return map;
  }

  public List<Cell> getAllCells()
  {
    List<Cell> cells = new ArrayList<Cell>();
    for (int y = 0; y < BOARD_SIZE; y++)
    {
      cells.addAll(getRow(y));
    }
    return cells;
  }

  public static int getQuadrantNumber(int x, int y)
  {
    // Quadrants numbered
    // 123
    // 456
    // 789
    return (y / 3) * 3 + x / 3;

  }

  public boolean isChanged()
  {
    return changed;
  }

  public void setChanged(boolean changed)
  {
    this.changed = changed;
  }

  public boolean sameBoard(Puzzle compare)
  {
    for (int y = 0; y < BOARD_SIZE; y++)
    {
      for (int x = 0; x < BOARD_SIZE; x++)
      {
        if (!getCellAt(x, y).sameCell(compare.getCellAt(x, y)))
        {
          return false;
        }
      }
    }
    return true;
  }

  public boolean isSolved()
  {
    for (int y = 0; y < BOARD_SIZE; y++)
    {
      for (int x = 0; x < BOARD_SIZE; x++)
      {
        if (getCellAt(x, y).getValue() == -1)
        {
          return false;
        }
      }
    }
    return true;
  }

}
