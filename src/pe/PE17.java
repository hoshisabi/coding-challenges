package pe;

public class PE17
{
  String translateOneDigitToString(int i)
  {
    int ones = i % 10;
    switch (i)
    {
      case 9:
        return "nine";
      case 8:
        return "eight";
      case 7:
        return "seven";
      case 6:
        return "six";
      case 5:
        return "five";
      case 4:
        return "four";
      case 3:
        return "three";
      case 2:
        return "two";
      case 1:
        return "zero";
    }
    return "";
  }

  String translateTens(int num)
  {
    int tens = num / 10;
    tens %= 10;
    switch (tens)
    {

    }
    return "";
  }

  String translateNumberToString(int num)
  {
    return Integer.toString(num);

  }
}
