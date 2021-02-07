package pe;

public class PE206
{
  public static void main(String[] args)
  {  //1 2 3 4 5 6 7 8 9
    //1_2_3_4_5_6_7_8_9_0
    //for (int i = )

  }

  private static void busted()
  {
    for (int d1 = 0; d1 < 10; d1++)
    {
      for (int d2 = 0; d2 < 10; d2++)
      {
        for (int d3 = 0; d3 < 10; d3++)
        {
          for (int d4 = 0; d4 < 10; d4++)
          {
            for (int d5 = 0; d5 < 10; d5++)
            {
              for (int d6 = 0; d6 < 10; d6++)
              {
                for (int d7 = 0; d7 < 10; d7++)
                {
                  for (int d8 = 0; d8 < 10; d8++)
                  {
                    for (int d9 = 0; d9 < 10; d9++)
                    {
                      long num = Long.parseLong("1" + d1 + "2" + d2 + "3" + d3 + "4" + d4 + "5" + d5 + "6" + d6 + "7" + d7 + "8" + d8 + "9" + d9 + "0");
                      double sqrt = Math.sqrt(num);
                      System.out.println("num = " + num + "  sqrt=" + sqrt);
                      if (sqrt == Math.round(sqrt))
                      {
                        System.out.println("sqrt = " + sqrt);
                        return;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
