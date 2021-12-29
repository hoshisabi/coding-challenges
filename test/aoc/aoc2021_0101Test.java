package aoc;

import junit.framework.TestCase;
import org.junit.Test;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.Arrays;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

public class aoc2021_0101Test extends TestCase
{

  public static final List<Integer> TEST_ARRAY = Arrays.asList(199, 200, 208, 210, 200, 207, 240, 269, 260, 263);

  @Test
  public void testDepthCount()
  {
    // Given this known set of distances
    List<Integer> testArray = TEST_ARRAY;

    // when I run the test count
    int counts = aoc2021_0101.countLarger(testArray);

    // then I get 7
    assertThat(counts).isEqualTo(7);
  }


  @Test
  public void testGetFromFile() throws IOException, URISyntaxException
  {
    List<Integer> integerList = aoc2021_0101.readFile("aoc2021_0101_testinput.txt");

    // then I get 7
    assertThat(integerList).isEqualTo(TEST_ARRAY);
  }
}