package aoc2021;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class aoc2021_0101
{
    public static int countLarger(List<Integer> depths) {
        int largerCount = 0;
        Integer lastCount = depths.get(0);
        for (Integer depth : depths) {
            if (lastCount < depth) {
                largerCount++;
            }
            lastCount = depth;
        }
        return largerCount;
    }

    public aoc2021_0101(String filename) throws IOException, URISyntaxException {
        URI uri = this.getClass().getResource(filename).toURI();
        List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
        int i = countLarger(lines.stream().map(Integer::parseInt).toList());
        System.out.println("i = " + i);
    }


    static void main(String[] args) {
        try {
//      aoc2021_0101 me = new aoc2021_0101("aoc-input/aoc2021_0101_testinput.txt");
            new aoc2021_0101("aoc-input/aoc2021_0101_input.txt");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


}
