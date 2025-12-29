package aoc_shared;

import java.io.IOException;
import java.nio.file.*;
import java.util.*;

public class DataLoader {
    private static final String DATA_ROOT = System.getenv( "AOC_DATA_PATH");

    public static List<String> loadInput(int year, int day, int part, boolean isTest) {
        Path yearDir = Paths.get(DATA_ROOT, String.valueOf(year));
        assert yearDir != null : "AOC_DATA_PATH environment variable is not set";

        List<String> patterns = new ArrayList<>();
        if (isTest) {
            patterns.add(String.format("aoc%dd%02dp%02d_test_input.txt", year, day, part));
            patterns.add(String.format("aoc%d_%02d%02d-test.txt", year, day, part)); // fallback
            patterns.add(String.format("aoc%d_%02d%02d_test.txt", year, day, part)); // fallback
            patterns.add(String.format("aoc%d_%02d%02d_testinput.txt", year, day, part)); // fallback
            patterns.add(String.format("aoc%d-%02d-%02d-test.txt", year, day, part));
            patterns.add(String.format("aoc%d_%02d%02d_testinput.txt", year, day, part));
            patterns.add(String.format("aoc%d-%02d-test.txt", year, day)); // fallback
            patterns.add(String.format("aoc%d_%02d%02d-test.txt", year, day, 1)); // fallback
            patterns.add(String.format("aoc%d_%02d%02d_testinput.txt", year, day, 1)); // fallback
        } else {
            patterns.add(String.format("aoc%d-%02d.txt", year, day));
            patterns.add(String.format("aoc%d-%02d%02d.txt", year, day,part));
            patterns.add(String.format("aoc%dd%02d_input.txt", year, day));
            patterns.add(String.format("aoc%d_%02d_input.txt", year, day));
            patterns.add(String.format("aoc%d_%02d%02d_input.txt", year, day, part));
            patterns.add(String.format("aoc%d_%02d%02d_input.txt", year, day, 1));
            patterns.add(String.format("aoc%d-%02d%02d.txt", year, day, 1));
        }

        for (String pattern : patterns) {
            Path path = yearDir.resolve(pattern);
            if (Files.exists(path)) {
                try {
                    return Files.readAllLines(path);
                } catch (IOException e) {
                    throw new RuntimeException("Failed to read " + path, e);
                }
            }
        }

        throw new RuntimeException("Could not find input for Year " + year + " Day " + day  + " Part " + part + " is_test=" + isTest);
    }
}