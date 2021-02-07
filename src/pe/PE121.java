package pe;

public class PE121
{
  private static class fraction
  {
    int numerator = 0;
    int denominator = 0;

    private fraction(int numerator, int denominator)
    {
      this.numerator = numerator;
      this.denominator = denominator;
      simplify();
    }

    private void simplify()
    {
      int g = gcd(Math.max(numerator, denominator), Math.min(numerator, denominator));
      numerator /= g;
      denominator /= g;
    }

    public static int gcd(int m, int n)
    {

      if (m < n)
      {
        int t = m;
        m = n;
        n = t;
      }

      int r = m % n;

      if (r == 0)
      {
        return n;
      }
      else
      {
        return gcd(n, r);
      }

    }

    public int getNumerator()
    {
      return numerator;
    }

    public int getDenominator()
    {
      return denominator;
    }

    public fraction add(fraction add)
    {
      int denom = add.getDenominator() * this.getDenominator();
      int numerator = add.getNumerator() * this.getDenominator() + this.getNumerator() * add.getDenominator();
      return new fraction(numerator, denom);
    }

    public String toString()
    {
      return numerator + "/" + denominator;
    }
  }

  public static void main(String[] args)
  {
    String s = "";
    fraction f = new fraction(1, 2);
    f = f.add(new fraction(1, 3));
    f = f.add(new fraction(1, 4));
    f = f.add(new fraction(1, 5));
    System.out.println("f = " + f);

  }
}
