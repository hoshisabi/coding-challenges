package pe;

public class PE28
{
  private static final long[][] spiral = new long[3][3];
  private static final int MID = spiral.length / 2;

  public static void main(String[] args)
  {
    long runningValue = 1;
    for (int offset = 0; offset < MID; offset++)
    {
      spiral[MID + offset][MID] = runningValue++;
    }
  }
}
