package pe;

public class PE162
{
  public static void main(String[] args)
  {                           //1234561234567890.
    long count = 0;
    long i = 0L;

    while (true)
    {
      i++;
      String str = Long.toString(i, 16);
      if (str.length() > 16)
      {
        break;
      }
      
      if (str.contains("0") && str.contains("1") && str.contains("a"))
      {
        count++;
      }
    }

    System.out.println("Long.toString(count, 16).toUpperCase() = " + Long.toString(count, 16).toUpperCase());
  }
}
