import importlib.util, pathlib
from aoc_tools import read_lines, time_call, aoc_input_path

def iter_solution_modules():
    base = pathlib.Path("src/aoc")
    for year_dir in sorted(base.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit(): continue
        year = int(year_dir.name)
        for f in sorted(year_dir.glob("day*.py")):
            day = int(f.stem[3:5])
            yield year, day, f

def import_module_from_path(path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore
    return mod

def main():
    total_t = 0.0
    for year, day, path in iter_solution_modules():
        mod = import_module_from_path(path)
        missing = [x for x in ("part1","part2") if not hasattr(mod, x)]
        if missing:
            print(f"[{year} Day {day:02d}] skipped (missing: {', '.join(missing)})")
            continue
        ipath = aoc_input_path(year, day, test=False)
        if not ipath.exists():
            print(f"[{year} Day {day:02d}] no input; skipping")
            continue
        lines = read_lines(ipath)
        ans1, t1 = time_call(mod.part1, lines)
        ans2, t2 = time_call(mod.part2, lines)
        total = t1 + t2
        total_t += total
        print(f"[{year} Day {day:02d}] p1={ans1} ({t1:.3f}s), p2={ans2} ({t2:.3f}s), total={total:.3f}s")
    print(f"Total time: {total_t:.3f}s")

if __name__ == "__main__":
    main()