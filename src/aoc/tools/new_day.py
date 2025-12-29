import argparse, pathlib
from aoc_tools import aoc_input_path, download_input

TEMPLATE = """def part1(lines: list[str]):
    # TODO: implement
    return None

def part2(lines: list[str]):
    # TODO: implement
    return None

if __name__ == "__main__":
    from aoc_tools import read_lines, time_call, aoc_input_path
    import sys
    year = {year}
    day = {day}
    test = "--test" in sys.argv
    ipath = aoc_input_path(year, day, test=test)
    lines = read_lines(ipath)
    ans1, t1 = time_call(part1, lines)
    ans2, t2 = time_call(part2, lines)
    print(f"Day {day:02d} {'(test)' if test else ''} - part1: {ans1} [{t1:.3f}s], part2: {ans2} [{t2:.3f}s]")
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("year", type=int)
    ap.add_argument("day", type=int)
    ap.add_argument("--no-download", action="store_true", help="Skip real input download")
    ap.add_argument("--with-test", action="store_true", help="Create empty test file")
    args = ap.parse_args()

    year, day = args.year, args.day
    # Create solution file
    sol = pathlib.Path("src") / "aoc" / f"{year}" / f"day{day:02d}.py"
    sol.parent.mkdir(parents=True, exist_ok=True)
    if not sol.exists():
        sol.write_text(TEMPLATE.format(year=year, day=day), encoding="utf-8")
        print(f"Created {sol}")
    else:
        print(f"Exists {sol}")

    # Inputs
    if not args.no-download:
        ipath = download_input(year, day)
        print(f"Downloaded {ipath}")
    if args.with-test:
        tpath = aoc_input_path(year, day, test=True)
        if not tpath.exists():
            tpath.write_text("", encoding="utf-8")
            print(f"Created empty test {tpath}")

if __name__ == "__main__":
    main()