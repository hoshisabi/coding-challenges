package aoc2021;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

@SuppressWarnings("CallToPrintStackTrace")
public class aoc2021_0102 {

    public static int countLarger(List<Integer> depths) {
        int largerCount = 0;
        Integer lastSum = null;

        // Sliding window of 3 elements
        for (int i = 0; i < depths.size() - 2; i++) {
            int sumAtDepth = depths.get(i) + depths.get(i + 1) + depths.get(i + 2);
            if (lastSum != null && lastSum < sumAtDepth) {
                largerCount++;
            }
            lastSum = sumAtDepth;
        }
        return largerCount;
    }

    public aoc2021_0102(String filename) throws IOException, URISyntaxException {
        URI uri = this.getClass().getResource(filename).toURI();
        List<String> lines = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
        int result = countLarger(lines.stream().map(Integer::parseInt).toList());
        System.out.println("Result: " + result);
    }


    public static void main(String[] args) {
        String filename = "aoc-input/aoc2021_0101_input.txt";
        try {
            new aoc2021_0102(filename);

        } catch (Exception e) {
            System.err.println("Could not read file: " + filename);
            e.printStackTrace();
        }
    }
}
