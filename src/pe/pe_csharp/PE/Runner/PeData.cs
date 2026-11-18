namespace PE.Runner;

/// <summary>
/// Locates <c>&lt;repo&gt;/data/pe</c> (or PE_DATA_PATH), which holds problem input files
/// and answers.txt. The directory is gitignored: Project Euler asks that answers and
/// supplied data not be republished.
/// </summary>
public static class PeData
{
    private static readonly Lazy<string> Root = new(FindRoot);

    public static string DataPath => Root.Value;

    public static string AnswersPath => Path.Combine(DataPath, "answers.txt");

    /// <summary>Reads a file a problem links to, e.g. <c>ReadAllLines("0022_names.txt")</c>.</summary>
    public static string[] ReadAllLines(string fileName)
    {
        var path = Path.Combine(DataPath, fileName);
        if (!File.Exists(path))
            throw new FileNotFoundException($"Download the problem's file to {path}", path);
        return File.ReadAllLines(path);
    }

    /// <summary>answers.txt: one "&lt;number&gt; &lt;answer&gt;" per line, written by <c>--accept</c>.</summary>
    public static Dictionary<int, string> ReadAnswers()
    {
        var result = new Dictionary<int, string>();
        if (!File.Exists(AnswersPath)) return result;
        foreach (var line in File.ReadAllLines(AnswersPath))
        {
            var parts = line.Split(' ', 2, StringSplitOptions.TrimEntries);
            if (parts.Length == 2 && int.TryParse(parts[0], out var n))
                result[n] = parts[1];
        }
        return result;
    }

    public static void WriteAnswers(Dictionary<int, string> answers)
    {
        Directory.CreateDirectory(DataPath);
        File.WriteAllLines(AnswersPath, answers.OrderBy(kv => kv.Key).Select(kv => $"{kv.Key} {kv.Value}"));
    }

    private static string FindRoot()
    {
        var configured = Environment.GetEnvironmentVariable("PE_DATA_PATH")?.Trim();
        if (!string.IsNullOrEmpty(configured)) return configured;

        foreach (var start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory })
        {
            for (var dir = new DirectoryInfo(start); dir != null; dir = dir.Parent)
            {
                if (Directory.Exists(Path.Combine(dir.FullName, ".git")))
                    return Path.Combine(dir.FullName, "data", "pe");
            }
        }
        throw new InvalidOperationException("PE_DATA_PATH is not set and no enclosing git repo was found.");
    }
}
