package pe;

public class PE15
{
  private static final int GRID_SIZE = 20;
  private static final long[][] paths = new long[GRID_SIZE + 1][GRID_SIZE + 1];

  public static void main(String[] args)
  {
    // First spot has a 1
    paths[0][0] = 1;

    // Go through all of the spots sequentially and add path
    for (int i = 0; i <= GRID_SIZE; i++)
    {
      for (int j = 0; j <= GRID_SIZE; j++)
      {
        if (i < GRID_SIZE)
        {
          paths[i + 1][j] += paths[i][j];
        }

        if (j < GRID_SIZE)
        {
          paths[i][j + 1] += paths[i][j];
        }
      }
    }

    System.out.println("Final count = " + paths[GRID_SIZE][GRID_SIZE]);
  }
}
