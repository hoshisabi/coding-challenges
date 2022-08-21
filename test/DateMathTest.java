import org.apache.commons.lang3.time.DateUtils;
import org.junit.Test;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class DateMathTest
{
  @Test
  public void testDate() throws ParseException
  {
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
    Date start = sdf.parse("2021-10-13");

    Date end = DateUtils.addDays(start, 180);
    System.out.println(end);
  }
}
