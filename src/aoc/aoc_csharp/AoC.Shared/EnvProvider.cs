namespace AoC.Shared;

/// <summary>
/// Settings lookup: process environment first, then the nearest <c>.env</c> file
/// (searched upward from the working directory and from the build output directory).
/// </summary>
public static class EnvProvider
{
    private static readonly Lazy<Dictionary<string, string>> DotEnv = new(LoadDotEnv);
    private static readonly Lazy<string?> DotEnvPath = new(() => FindUp(".env", isDirectory: false));
    private static readonly Lazy<string?> RepoRoot = new(() =>
        FindUp(".git", isDirectory: true) is { } git ? Path.GetDirectoryName(git) : null);

    private static string? _dataPath;

    /// <summary>Returns the value from the environment or .env, or null when unset or empty.</summary>
    public static string? Get(string key)
    {
        var value = Environment.GetEnvironmentVariable(key)?.Trim();
        if (!string.IsNullOrEmpty(value)) return value;
        return DotEnv.Value.TryGetValue(key, out var fromFile) && fromFile.Length > 0 ? fromFile : null;
    }

    /// <summary>
    /// AOC_DATA_PATH from the environment or .env. When neither sets it,
    /// falls back to <c>&lt;repo root&gt;/data/aoc</c>.
    /// </summary>
    public static string GetBaseDataPath()
    {
        if (_dataPath != null) return _dataPath;

        var configured = Get("AOC_DATA_PATH");
        if (configured != null)
        {
            if (!Directory.Exists(configured))
            {
                var source = Environment.GetEnvironmentVariable("AOC_DATA_PATH") is { Length: > 0 }
                    ? "the AOC_DATA_PATH environment variable"
                    : DotEnvPath.Value ?? ".env";
                throw new DirectoryNotFoundException(
                    $"AOC_DATA_PATH is '{configured}' (from {source}), but that directory does not exist.");
            }
            return _dataPath = configured;
        }

        if (RepoRoot.Value is { } root && Directory.Exists(Path.Combine(root, "data", "aoc")))
            return _dataPath = Path.Combine(root, "data", "aoc");

        throw new InvalidOperationException(
            "AOC_DATA_PATH is not set (environment or .env) and <repo>/data/aoc was not found.");
    }

    private static Dictionary<string, string> LoadDotEnv()
    {
        var result = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        if (DotEnvPath.Value is not { } path) return result;

        foreach (var raw in File.ReadAllLines(path))
        {
            var line = raw.Trim();
            if (line.Length == 0 || line.StartsWith('#')) continue;
            var eq = line.IndexOf('=');
            if (eq <= 0) continue;

            var value = line[(eq + 1)..].Trim();
            if (value.Length >= 2 && (value[0] == '"' || value[0] == '\'') && value[^1] == value[0])
                value = value[1..^1];
            result[line[..eq].Trim()] = value;
        }
        return result;
    }

    private static string? FindUp(string name, bool isDirectory)
    {
        foreach (var start in new[] { Directory.GetCurrentDirectory(), AppContext.BaseDirectory })
        {
            for (var dir = new DirectoryInfo(start); dir != null; dir = dir.Parent)
            {
                var candidate = Path.Combine(dir.FullName, name);
                if (isDirectory ? Directory.Exists(candidate) : File.Exists(candidate))
                    return candidate;
            }
        }
        return null;
    }
}
