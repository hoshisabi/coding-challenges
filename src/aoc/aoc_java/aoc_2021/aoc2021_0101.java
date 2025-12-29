package aoc_2021;

import aoc_shared.DataLoader;

import java.io.IOException;
import java.net.URISyntaxException;
import java.util.List;

public class aoc2021_0101 {
    public static int countLarger(List<Integer> depths) {
        int largerCount = 0;
        Integer lastCount = depths.getFirst();
        for (Integer depth : depths) {
            if (lastCount < depth) {
                largerCount++;
            }
            lastCount = depth;
        }
        return largerCount;
    }

    public aoc2021_0101(boolean isTest) throws IOException, URISyntaxException {
        List<String> lines = DataLoader.loadInput(2021, 1, 1, isTest);
        int i = countLarger(lines.stream().map(Integer::parseInt).toList());
        System.out.println("i = " + i);
    }


    static void main(String[] args) {
        try {
//      aoc2021_0101 me = new aoc2021_0101(true);
            new aoc2021_0101(false);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }


}
