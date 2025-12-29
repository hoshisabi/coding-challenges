package aoc_2021;

import aoc_shared.DataLoader;

import java.util.List;
import java.util.Locale;

public class aoc2021_0202 {

    public static int part2Navigate(List<String> directions) {
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
        List<String> lines = DataLoader.loadInput(2021, 2, 2, false);
        System.out.println(part2Navigate(lines));
    }
}


