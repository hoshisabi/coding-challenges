package pe;

import junit.framework.TestCase;
import org.junit.Test;

public class PEUtilTest extends TestCase
{
  @Test
  public void testPrime()
  {
    assertTrue("five should be prime", PEUtil.isPrime(5));
    assertFalse("twelve should not be prime", PEUtil.isPrime(12));
    assertTrue("seventeen should be prime", PEUtil.isPrime(17));
    assertFalse("FOURTEEN should not be prime", PEUtil.isPrime(14));
    assertTrue("seventeen should be prime", PEUtil.isPrime(13));
    assertTrue("three should be prime", PEUtil.isPrime(3));
    assertFalse("21598L should not be prime", PEUtil.isPrime(21598L));
    assertTrue("21599L should be prime", PEUtil.isPrime(21599L));
    assertFalse("31599L should not be prime", PEUtil.isPrime(31599L));
  }
}