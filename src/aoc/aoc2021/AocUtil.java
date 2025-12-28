package aoc2021;

import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Objects;
import java.io.IOException;

public class AocUtil {
    public static List<String> readLines(String resourcePath) throws IOException, URISyntaxException {
        URI uri = Objects.requireNonNull(
                Thread.currentThread().getContextClassLoader().getResource(resourcePath),
                "Resource not found: " + resourcePath
        ).toURI();
        return Files.readAllLines(Paths.get(uri), Charset.defaultCharset());
    }

    public static List<Integer> readIntegers(String resourcePath) throws IOException, URISyntaxException {
        return readLines(resourcePath).stream().map(Integer::valueOf).toList();
    }
}
