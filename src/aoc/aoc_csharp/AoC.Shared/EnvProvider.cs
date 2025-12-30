namespace AoC.Shared;

public static class EnvProvider
{
    private static string? _dataPath;

    public static string GetBaseDataPath()
    {
        if (_dataPath != null) return _dataPath;

        var dir = Environment.GetEnvironmentVariable("AOC_DATA_PATH")?.Trim();
        
        if (string.IsNullOrEmpty(dir))
        {
            throw new InvalidOperationException(
                "AOC_DATA_PATH environment variable not set! " +
                "Check your .env file or IDE Run Configuration.");
        }

        if (!Directory.Exists(dir))
        {
            throw new DirectoryNotFoundException($"AOC_DATA_PATH is set to '{dir}', but that directory does not exist.");
        }

        _dataPath = dir;
        return _dataPath;
    }
}