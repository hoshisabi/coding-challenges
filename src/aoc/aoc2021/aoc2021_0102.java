package aoc2021;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

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

    public static void main(String[] args) {
        // Path relative to your project root where you moved the files
        Path inputPath = Paths.get("aoc-input/aoc2021_0101_input.txt");

        try {
            // Read all lines, convert to Integers
            List<Integer> depths = Files.lines(inputPath)
                    .map(String::trim)
                    .filter(line -> !line.isEmpty())
                    .map(Integer::parseInt)
                    .collect(Collectors.toList());

            int result = countLarger(depths);
            System.out.println("Result: " + result);

        } catch (IOException e) {
            System.err.println("Could not read file: " + inputPath.toAbsolutePath());
            e.printStackTrace();
        } catch (NumberFormatException e) {
            System.err.println("Error parsing integer from file.");
            e.printStackTrace();
        }
    }
}