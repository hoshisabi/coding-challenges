using System.Net;

namespace AoC.Shared;

/// <summary>
/// Input file layout under the data root:
/// <code>
///   &lt;root&gt;/&lt;year&gt;/aoc2026-03.txt              real input (downloaded)
///   &lt;root&gt;/&lt;year&gt;/aoc2026-03-test.txt         example input (pasted by hand)
///   &lt;root&gt;/&lt;year&gt;/aoc2026-03-test2.txt        more examples: anything matching -test*.txt
///   &lt;root&gt;/&lt;year&gt;/aoc2026-03-test.expected    optional: line 1 = part 1 answer, line 2 = part 2
/// </code>
/// </summary>
public static class InputFiles
{
    private static readonly HttpClient Http = CreateClient();

    public static string YearDir(int year) => Path.Combine(EnvProvider.GetBaseDataPath(), year.ToString());

    public static string RealPath(int year, int day) => Path.Combine(YearDir(year), $"aoc{year}-{day:D2}.txt");

    public static string TestPath(int year, int day) => Path.Combine(YearDir(year), $"aoc{year}-{day:D2}-test.txt");

    public static IReadOnlyList<string> TestPaths(int year, int day)
    {
        var dir = YearDir(year);
        if (!Directory.Exists(dir)) return [];
        return Directory.GetFiles(dir, $"aoc{year}-{day:D2}-test*.txt").Order(StringComparer.Ordinal).ToList();
    }

    public static string ExpectedPath(string inputPath) => Path.ChangeExtension(inputPath, ".expected");

    /// <summary>
    /// Expected answers for an input file, or nulls when there is no .expected file.
    /// An empty line or "?" leaves that part unchecked.
    /// </summary>
    public static (string? Part1, string? Part2) ReadExpected(string inputPath)
    {
        var path = ExpectedPath(inputPath);
        if (!File.Exists(path)) return (null, null);
        var lines = File.ReadAllLines(path);
        return (Clean(lines.ElementAtOrDefault(0)), Clean(lines.ElementAtOrDefault(1)));

        static string? Clean(string? s) => s?.Trim() is { Length: > 0 } t && t != "?" ? t : null;
    }

    /// <summary>Puzzles unlock at midnight US Eastern (UTC-5 in December).</summary>
    public static DateTimeOffset UnlockTime(int year, int day) => new(year, 12, day, 0, 0, 0, TimeSpan.FromHours(-5));

    /// <summary>
    /// Downloads the real input if it isn't already on disk. Needs AOC_SESSION (environment or .env).
    /// Returns false with a reason instead of throwing, so the runner can keep going.
    /// </summary>
    public static bool TryDownload(int year, int day, out string message)
    {
        var path = RealPath(year, day);
        if (File.Exists(path))
        {
            message = $"already have {path}";
            return true;
        }

        if (DateTimeOffset.UtcNow < UnlockTime(year, day))
        {
            message = $"{year} day {day} unlocks at {UnlockTime(year, day).ToLocalTime():yyyy-MM-dd HH:mm} local time";
            return false;
        }

        var session = EnvProvider.Get("AOC_SESSION");
        if (session == null)
        {
            message = "AOC_SESSION is not set (environment or .env); can't download input";
            return false;
        }

        using var request = new HttpRequestMessage(HttpMethod.Get, $"https://adventofcode.com/{year}/day/{day}/input");
        request.Headers.Add("Cookie", $"session={session}");
        using var response = Http.Send(request);
        if (response.StatusCode != HttpStatusCode.OK)
        {
            message = $"download failed: HTTP {(int)response.StatusCode} {response.ReasonPhrase}" +
                      (response.StatusCode is HttpStatusCode.BadRequest or HttpStatusCode.InternalServerError
                          ? " (AOC_SESSION may have expired)"
                          : "");
            return false;
        }

        var text = response.Content.ReadAsStringAsync().GetAwaiter().GetResult();
        Directory.CreateDirectory(YearDir(year));
        File.WriteAllText(path, text.Replace("\r\n", "\n").TrimEnd('\n') + "\n");
        message = $"downloaded {path}";
        return true;
    }

    private static HttpClient CreateClient()
    {
        var client = new HttpClient { Timeout = TimeSpan.FromSeconds(30) };
        // AoC asks automated tools to identify themselves.
        client.DefaultRequestHeaders.UserAgent.ParseAdd(
            "hoshisabi-coding-challenges/1.0 (+https://github.com/hoshisabi/coding-challenges)");
        return client;
    }
}
