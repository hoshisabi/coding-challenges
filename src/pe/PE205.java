package pe;

import java.util.*;

public class PE205
{
  public static void main(String[] args)
  {
    long winCount = 0l;
    long totalsCount = 0l;

    for (int sixA = 1; sixA <= 6; sixA++)
    {
      for (int sixB = 1; sixB <= 6; sixB++)
      {
        for (int sixC = 1; sixC <= 6; sixC++)
        {
          for (int sixD = 1; sixD <= 6; sixD++)
          {
            for (int sixE = 1; sixE <= 6; sixE++)
            {
              for (int sixF = 1; sixF <= 6; sixF++)
              {
                int sixTot = sixA + sixB + sixC + sixD + sixE + sixF;
                System.out.println("sixTot = " + sixTot);
                for (int fourA = 1; fourA <= 4; fourA++)
                {
                  for (int fourB = 1; fourB <= 4; fourB++)
                  {
                    for (int fourC = 1; fourC <= 4; fourC++)
                    {
                      for (int fourD = 1; fourD <= 4; fourD++)
                      {
                        for (int fourE = 1; fourE <= 4; fourE++)
                        {
                          for (int fourF = 1; fourF <= 4; fourF++)
                          {
                            for (int fourG = 1; fourG <= 4; fourG++)
                            {
                              for (int fourH = 1; fourH <= 4; fourH++)
                              {
                                for (int fourI = 1; fourI <= 4; fourI++)
                                {
                                  int fourTot = fourA + fourB + fourC + fourD + fourE + fourF + fourG + fourH + fourI;
                                  System.out.println("  fourTot= " + fourTot);

                                  totalsCount++;
                                  if (fourTot > sixTot)
                                  {
                                    winCount++;
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
          }
        }
      }
    }
    System.out.println("totalsCount = " + totalsCount);
    System.out.println("winCount = " + winCount);
  }

}
