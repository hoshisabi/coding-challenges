# Advent of Code — C#

One project per year (`AoC.YearNNNN`), all sharing `AoC.Shared`. Each `Program.cs` is one line:
the runner finds every `IDay` class in the project by reflection, so adding a day never means
editing `Program.cs`.

## Daily loop

```powershell
cd src/aoc/aoc_csharp
./new-day.ps1                # today's puzzle in December, otherwise the next missing day
# paste the example into the -test.txt file it prints, and the answers into -test.expected
./aoc.ps1 -t -Watch          # re-runs the examples on every save, with ✓ / ✗ per part
./aoc.ps1                    # examples, then the real input
```

`new-day.ps1` creates `DayNN.cs` (both parts throw `NotImplementedException`, which shows as
"not implemented"), the empty example files, and downloads the real input. For a new year it also
creates the project and adds it to `coding-challenges.sln`: `./new-day.ps1 -Year 2027 -ProjectOnly`.

## Runner options

`./aoc.ps1 [days] [options]` runs `dotnet run` on the latest year's project (`-Year 2025` picks
another; `-Watch` uses `dotnet watch`). Everything else goes to the runner:

| Argument        | Effect                                                              |
|-----------------|---------------------------------------------------------------------|
| `3`, `1 4`, `1-5`, `all` | Which days. Default: the highest-numbered day in the project |
| `-t`, `--test`  | Examples only                                                       |
| `-r`, `--real`  | Real input only                                                     |
| `--fetch`       | Download real inputs for the chosen days, then exit                 |
| `--no-warmup`   | Skip the untimed JIT warm-up before timing the real input           |
| `--print-data-path` | Show which input directory is in use                            |

Exit code is 1 when a `.expected` check fails or a part throws, 0 otherwise.

## Input files

Under the data root, per year:

| File                          | Contents                                              |
|-------------------------------|-------------------------------------------------------|
| `aoc2026-03.txt`              | Real input; downloaded on first run if missing        |
| `aoc2026-03-test.txt`         | Example input, pasted by hand                         |
| `aoc2026-03-test2.txt`, ...   | More examples; every `-test*.txt` file runs            |
| `aoc2026-03-test.expected`    | Optional. Line 1 = part 1 answer, line 2 = part 2; `?` or blank = unchecked |

Each input gets a fresh instance of the day class, so fields don't carry over between inputs.

## Configuration

Read from the process environment first, then the nearest `.env` (repo root):

- `AOC_DATA_PATH`: data root. When unset, falls back to `<repo>/data/aoc`.
- `AOC_SESSION`: the `session` cookie from adventofcode.com, needed for downloads.
  Downloads are skipped before a puzzle unlocks (midnight US Eastern).
