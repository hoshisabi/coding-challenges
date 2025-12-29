package aoc2021;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Locale;

public class aoc2021_0201 {

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


    public aoc2021_0201(String filename) throws IOException, URISyntaxException {
        URI uri = this.getClass().getResource(filename).toURI();
        List<String> values = Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
        System.out.println(navigate(values));
    }


    static void main() {
        try {
            new aoc2021_0201("aoc-input/aoc2021_0201_input.txt");
        } catch (Exception e) {
            e.printStackTrace();
            return;
        }
    }
}


