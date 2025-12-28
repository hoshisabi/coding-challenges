package aoc2021;

import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Locale;

public class aoc2021_0201 {
    public static List<String> readFileStrings(String filename) throws IOException, URISyntaxException {
        return Files.readAllLines(Paths.get(aoc2021_0201.class.getResource(filename).toURI()), Charset.defaultCharset())
                .stream()
                .toList();
    }

    public static int navigate(List<String> directions) {
        int hor = 0;
        int depth = 0;
        int aim = 0;

        for (String direction : directions) {
            String[] parts = direction.split(" ");
            int num = Integer.parseInt(parts[1]);
            String dir = parts[0].toLowerCase(Locale.ROOT);
            if (dir.equals("forward")) {
                hor += num;
                depth += aim * num;
            } else if (dir.equals("up")) {
                aim -= num;
            } else if (dir.equals("down")) {
                aim += num;
            } else {
                System.out.println("Unknown direction: '" + dir + "', num=" + num + ": " + direction);
            }
        }
        return hor * depth;
    }


    public static int oldNavigate(String[] directions) {
        int hor = 0;
        int depth = 0;

        for (String direction : directions) {
            String[] parts = direction.split(" ");
            int num = Integer.valueOf(parts[1]);
            String dir = parts[0].toLowerCase(Locale.ROOT);
            if (dir.equals("forward")) {
                hor += num;
            } else if (dir.equals("up")) {
                depth -= num;
            } else if (dir.equals("down")) {
                depth += num;
            } else {
                System.out.println("Unknown direction: '" + dir + "', num=" + num + ": " + direction);
            }
        }
        return hor * depth;
    }

    static void main() {
        List<String> values;
        try {
            values = AocUtil.readLines("aoc-input/aoc2021_0201_input.txt");
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }
        System.out.println(navigate(values));
    }
}

