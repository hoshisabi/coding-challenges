using System.Text;

namespace AoC.Shared;

public static class StringExtensions
{
    public static string Repeat(this string value, int count)
    {
        if (count <= 0) return string.Empty;
        if (count == 1) return value;
        
        var sb = new StringBuilder(value.Length * count);
        for (int i = 0; i < count; i++)
        {
            sb.Append(value);
        }
        return sb.ToString();
    }
}