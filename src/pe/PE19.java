package pe;

import java.util.*;

public class PE19
{
  public static void main(String[] args)
  {
    Calendar cal = Calendar.getInstance();
    cal.set(2001, 1, 1);
    Date endOfCentury = cal.getTime();
    System.out.println("endOfCentury = " + endOfCentury);

    cal.set(1901, 1, 1);
    System.out.println("cal.getTime() = " + cal.getTime());
    int number = 0;
    while (cal.getTime().before(endOfCentury))
    {
      System.out.println("cal.getTime() = " + cal.getTime());
      System.out.println("cal.get(Calendar.DAY_OF_WEEK) = " + cal.get(Calendar.DAY_OF_WEEK));
      if (cal.get(Calendar.DAY_OF_WEEK) == Calendar.SUNDAY)
      {
        number++;
      }
      cal.add(Calendar.MONTH, 1);
    }

    System.out.println("number = " + number);
  }


}