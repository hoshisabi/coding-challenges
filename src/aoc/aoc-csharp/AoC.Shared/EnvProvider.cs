namespace AoC.Shared;

public static class EnvProvider
{
    private static string? _dataPath;

    public static string GetBaseDataPath()
    {
        if (_dataPath != null) return _dataPath;

        // 1. Find the .env file by walking up from the executable
        var dir = new DirectoryInfo(AppContext.BaseDirectory);
        while (dir != null && !File.Exists(Path.Combine(dir.FullName, ".env")))
        {
            dir = dir.Parent;
        }

        if (dir == null) throw new Exception("Could not find .env file at Git Root!");

        // 2. Simple parser for AOC_DATA_PATH=...
        var envLine = File.ReadLines(Path.Combine(dir.FullName, ".env"))
            .FirstOrDefault(l => l.StartsWith("AOC_DATA_PATH="));

        _dataPath = envLine?.Split('=')[1].Trim() 
                    ?? throw new Exception("AOC_DATA_PATH not defined in .env");

        return _dataPath;
    }

}