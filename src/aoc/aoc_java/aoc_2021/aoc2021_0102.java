package aoc_2021;

import aoc_shared.DataLoader;

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

    static void main(String[] args)
    {
        List<String> lines = DataLoader.loadInput(2021, 1, 2, true);
        int result = countLarger(lines.stream().map(Integer::parseInt).toList());
        System.out.println("result = " + result);
    }
}
