# Project Euler in C#

Goal: use Project Euler to practice C# and the math PE leans on (dynamic programming in
particular), with Claude as a tutor rather than a solver. Started 2026-11-18.

## Decisions

- **Separate project, not an AoC year.** `src/pe/pe_csharp/PE` is one exe project with its own
  small runner (`Runner/`). It copies the AoC runner's pattern (reflection discovery, ✓/✗,
  timing, `dotnet watch`) but doesn't reference `AoC.Shared`: PE has one answer per problem,
  no input file in most problems, and given small cases instead of example inputs.
- **Small cases are `Checks` in code**, not files. A failing check skips the solve, since PE
  solves can take minutes.
- **Answers live in `data/pe/answers.txt`** (gitignored). The repo is public, and PE asks that
  answers not be published. Whether to commit solutions past problem 100 is still open; for now
  they're committed like the rest of the repo.
- **No JIT warm-up by default** (`--warmup` opts in). AoC warms up because its solves are fast.
- **Problem 2 is the demo**, ported from `src/pe/PE2.java` (solved years ago), so the scaffold
  doesn't solve a new problem.
- **Tutor skill** at `.claude/skills/tutor/`: hints in steps of increasing detail, no solution
  code, and pushback when the request is "just tell me".
- **The RPS(n) problem** (generalised Rock-Paper-Scissors, S(10⁵)) was solved by Claude in
  Python before this project existed, so it doesn't count as Dan's. Write-up in the journal.
  Its PE number wasn't in the pasted text. It's a candidate for Dan to re-derive in C#
  with the tutor, using the write-up as a hint sheet rather than as code to copy.

## Tasks

- [x] Runner, `pe.ps1`, `new-problem.ps1`, Problem 2, README
- [x] Tutor skill draft
- [ ] Dan: try the tutor skill on a real problem and adjust it
- [ ] Dan: port a few old Java solutions (`src/pe/*.java`) to practice C# with known answers
- [ ] Dan: start `PE/Lib/` (primes sieve, gcd, modular power, an exact fraction type) when a
      problem needs it, not ahead of time
- [ ] Dan: dynamic programming practice. Unsolved candidates: 76, 81, 82, 114–117 (83 is the
      same grid as 81/82 but needs a shortest-path search instead). Solved in Java already, so
      good for checking a new DP approach against an old answer: 15, 18, 31, 67.
