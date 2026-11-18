namespace PE.Runner;

/// <summary>
/// One Project Euler problem. The runner finds every implementation by reflection.
/// </summary>
public interface IProblem
{
    int Number { get; }

    /// <summary>
    /// Small cases with known answers, usually the ones the problem statement gives
    /// ("you are given S(10) = ..."). They run before <see cref="Solve"/>, and a failure
    /// skips the solve.
    /// </summary>
    IEnumerable<Check> Checks => [];

    /// <summary>The answer to submit. Return a number or a string; it is printed invariant-culture.</summary>
    object Solve();
}

/// <param name="Label">What is being checked, e.g. "S(10)".</param>
/// <param name="Compute">Produces the value; compared to <paramref name="Expected"/> as invariant-culture text.</param>
/// <param name="Expected">The known answer, written exactly as the value should print, e.g. "1.1546112276".</param>
public sealed record Check(string Label, Func<object> Compute, string Expected);
