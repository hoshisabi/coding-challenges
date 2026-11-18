# Project Euler — C#

One project, `PE`. `Program.cs` is one line: the runner finds every `IProblem` class by
reflection, so adding a problem never means editing `Program.cs`. Built on the same pattern as
`src/aoc/aoc_csharp`, adjusted for how PE problems are shaped:

| AoC                               | PE                                                        |
|-----------------------------------|-----------------------------------------------------------|
| Two parts per day                 | One answer per problem                                    |
| Example input files + `.expected` | `Checks`: the small cases the statement gives ("S(10) = …") |
| Real input file                   | Usually none; the few that have one read it with `PeData.ReadAllLines` |

## Loop

```powershell
cd src/pe/pe_csharp
./new-problem.ps1 31          # creates PE/Problems/Problem0031.cs
# add the statement's small cases to Checks first
./pe.ps1 31 -c -Watch         # re-runs the checks on every save
./pe.ps1 31                   # checks, then the solve (skipped if a check fails)
./pe.ps1 31 --accept          # after the site accepts the answer: record it
```

The usual way into a hard problem is the same each time: write a slow method that's clearly
correct, run it on small cases, print the structure of the results (not only the numbers), guess
the rule, write the fast method, and check the fast method against the slow one. Both methods can
live in the same class, with the slow one checked against the fast one in `Checks`.

## Runner options

`./pe.ps1 [problems] [options]`; `-Watch` uses `dotnet watch`, everything else goes to the runner.

| Argument                  | Effect                                                   |
|---------------------------|----------------------------------------------------------|
| `31`, `2 5 9`, `1-10`, `all` | Which problems. Default: the highest-numbered one     |
| `-c`, `--checks`          | Checks only                                              |
| `--accept`                | Record each solved answer in `answers.txt`, replacing any recorded one |
| `--warmup`                | Untimed solve before the timed one (off by default; solves can take minutes) |
| `--print-data-path`       | Show the data directory                                  |

Exit code is 1 when a check fails, an answer differs from `answers.txt`, or something throws.

## Data

`<repo>/data/pe` (or `PE_DATA_PATH`), gitignored:

- `answers.txt`: `<number> <answer>` per line, written by `--accept`. Once recorded, every run
  shows ✓ or ✗ against it, so `./pe.ps1 all` works as a regression run after changing shared code.
- Input files a problem links to (e.g. problem 22's names list).

Project Euler asks that answers, and solutions past problem 100, not be published. This repo is
public on GitHub, which is why answers stay under `data/`. Solutions in `PE/Problems` are
committed like everything else here.
