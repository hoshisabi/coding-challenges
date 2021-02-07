package pe;

public class PE135
{
  static int countSolutions(int n)
  {
    int count = 0;
    for (int z = 1; z < Math.sqrt(n); z++)
    {
      for (int step = 1; step < n; step++)
      {
        int y = z + step;
        int x = y + step;

        if ((x * x) - (y * y) - (z * z) == n)
        {
          count++;
        }
      }
    }

    return count;
  }

  public static void main(String[] args)
  {
    System.out.println("countSolutions(27) = " + countSolutions(27));
    System.out.println("countSolutions(1155) = " + countSolutions(1155));

    int count = 0;
    for (int i = 1; i < 1000000; i++)
    {
      if (countSolutions(i) == 10)
      {
        count++;
      }
    }

    System.out.println("count = " + count);
  }
}
