package aoc2021;

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

    public static void main(String[] args) {
        String filename = "aoc-input/aoc2021_0101_input.txt";
        try {
            var depths = aoc2021_0101.readFileIntegers(filename);
            int result = countLarger(depths);
            System.out.println("Result: " + result);

        } catch (Exception e) {
            System.err.println("Could not read file: " + filename);
            e.printStackTrace();
        }
    }
}