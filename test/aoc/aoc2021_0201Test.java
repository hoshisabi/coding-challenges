package aoc;

import junit.framework.TestCase;
import org.junit.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class aoc2021_0201Test extends TestCase
{
  @Test
  public void testOldInput()
  {
    String[] testInputs = ("forward 5\n" +
        "down 5\n" +
        "forward 8\n" +
        "up 3\n" +
        "down 8\n" +
        "forward 2").split("\n");

    int results = aoc2021_0201.oldNavigate(testInputs);
    assertThat(results).isEqualTo(150);
  }

  @Test
  public void testInput()
  {
    String[] testInputs = ("forward 5\n" +
        "down 5\n" +
        "forward 8\n" +
        "up 3\n" +
        "down 8\n" +
        "forward 2").split("\n");

    int results = aoc2021_0201.navigate(testInputs);
    assertThat(results).isEqualTo(900);
  }
}