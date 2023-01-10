package aoc2021;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class aoc2021_0802
{

  public static class Digit
  {
    String segments;
    int value = -1;

    public Digit(String inputSegments)
    {
      Stream<String> sorted = Arrays.stream(inputSegments.split("")).sorted();
      segments = sorted.collect(Collectors.joining());
    }

    public int getValue()
    {
      return value;
    }

    public void setValue(int value)
    {
      this.value = value;
    }

    public String getSegments()
    {
      return segments;
    }

    public int getSegmentLength()
    {
      return segments.length();
    }

    @Override
    public boolean equals(Object o)
    {
      if (this == o)
      {
        return true;
      }
      if (o == null || getClass() != o.getClass())
      {
        return false;
      }
      Digit digit = (Digit) o;
      return Objects.equals(segments, digit.segments);
    }

    public String missingSegment(String compareSegment)
    {
      for (String segment : compareSegment.split(""))
      {
        if (!containsAll(segment))
        {
          return segment;
        }
      }
      return "";
    }

    public boolean containsAny(String checkSegment)
    {
      for (String segment : checkSegment.split(""))
      {
        if (segments.contains(segment))
        {
          return true;
        }
      }
      return false;
    }

    public boolean containsAll(String checkSegment)
    {
      for (String segment : checkSegment.split(""))
      {
        if (!segments.contains(segment))
        {
          return false;
        }
      }
      return true;
    }

    @Override
    public int hashCode()
    {
      return Objects.hash(segments);
    }

    @Override
    public String toString()
    {
      return "Digit{" +
          "segments='" + segments + '\'' +
          ", value=" + value +
          '}';
    }
  }


  public static class DigitMap
  {
    List<Digit> digits;
    Digit[] digitArr;

    public List<Digit> getDigits()
    {
      return digits;
    }

    public int decodeSegments(String segments)
    {
      Digit checkDigit = new Digit(segments);
      for (Digit digit : digits)
      {
        if (digit.equals(checkDigit))
        {
          return digit.getValue();
        }
      }
      return -1;
    }

    public void determineValues()
    {
      List<Digit> unmapped = new ArrayList<>();
      digitArr = new Digit[10];

      for (Digit d : digits)
      {
        String digitString = d.getSegments();
        if (digitString.length() == 2)
        {
          d.setValue(1);
          digitArr[d.getValue()] = d;
        }
        else if (digitString.length() == 3)
        {
          d.setValue(7);
          digitArr[d.getValue()] = d;
        }
        else if (digitString.length() == 4)
        {
          d.setValue(4);
          digitArr[d.getValue()] = d;
        }
        else if (digitString.length() == 7)
        {
          d.setValue(8);
          digitArr[d.getValue()] = d;
        }
        else
        {
          unmapped.add(d);
        }
      }

      String sevenSegments = digitArr[7].getSegments();
      String topBarSegment = digitArr[1].missingSegment(sevenSegments);

      for (Digit digit : unmapped)
      {
        if (!digit.containsAny(topBarSegment))
        {
          digit.setValue(4);
          digitArr[4] = digit;
          break;
        }
      }
      unmapped.remove(digitArr[4]);

      for (Digit digit : unmapped)
      {
        if (digit.getSegments().length() == 6)
        {
          if (!digit.containsAll(digitArr[1].getSegments()))
          {
            digit.setValue(6);
            digitArr[6] = digit;
            break;
          }
        }
      }
      unmapped.remove(digitArr[6]);

      String topRightBar = digitArr[6].missingSegment(digitArr[8].getSegments());
      for (Digit digit : unmapped)
      {
        if (!digit.containsAll(topRightBar))
        {
          digit.setValue(5);
          digitArr[5] = digit;
          break;
        }
      }
      unmapped.remove(digitArr[5]);

      String bottomLeft = digitArr[5].missingSegment(digitArr[6].getSegments());
      for (Digit digit : unmapped)
      {
        if (!digit.containsAll(bottomLeft))
        {
          if (digit.getSegmentLength() == 6)
          {
            digit.setValue(9);
            digitArr[9] = digit;
          }
          else if (digit.getSegmentLength() == 5)
          {
            digit.setValue(3);
            digitArr[3] = digit;
          }
        }
        else
        {
          if (digit.getSegmentLength() == 6)
          {
            digit.setValue(0);
            digitArr[0] = digit;
          }
          else
          {
            digit.setValue(2);
            digitArr[2] = digit;
          }
        }
      }
    }


    public DigitMap(String[] digitKey)
    {
      digits = new ArrayList<>();

      for (String digitString : digitKey)
      {
        digits.add(new Digit(digitString));
      }
      determineValues();
    }

    @Override
    public String toString()
    {
      return "DigitMap{" +
          "digits=" + digits +
          '}';
    }
  }

  public aoc2021_0802(String filename) throws IOException, URISyntaxException
  {
    URI uri = this.getClass().getResource(filename).toURI();
    List<String> strings = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    System.out.println(strings);

    int sum = 0;
    for (String string : strings)
    {
      // We can throw out everything before the |
      String[] split = string.split("\\|");
      String keyLine = split[0].trim();
      String readingLine = split[1].trim();
      String[] readingDigits = readingLine.split("\\s");
      String[] keyDigits = keyLine.split("\\s");
      DigitMap dm = new DigitMap(keyDigits);

      int subtotal = 0;
      for (String oneDigit : readingDigits)
      {
        subtotal *= 10;
        subtotal += dm.decodeSegments(oneDigit);
      }
      System.out.println("readingDigits = " + Arrays.toString(readingDigits) + " = " + subtotal);
      sum += subtotal;
    }

    System.out.println("** TOTAL sum = " + sum);
  }

  public static void main(String[] args)
  {
    try
    {
//      aoc2021_0802 me = new aoc2021_0802("aoc2021_0801_testinput.txt");
      aoc2021_0802 me = new aoc2021_0802("aoc2021_0801_input.txt");
    }
    catch (Exception e)
    {
      e.printStackTrace();
    }
  }
}
