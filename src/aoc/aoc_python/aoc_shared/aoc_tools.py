from pathlib import Path
import os, time, requests

AOC_BASE = "https://adventofcode.com"

def get_data_root():
    """Finds the data root from .env by walking up the tree."""
    current = Path(__file__).resolve()
    while current != current.parent:
        if (current / ".env").exists():
            break
        current = current.parent

    with open(current / ".env") as f:
        for line in f:
            if line.startswith("AOC_DATA_PATH="):
                return Path(line.split("=")[1].strip())
    raise RuntimeError("AOC_DATA_PATH not found in .env")

def get_input_path(year: int, day: int, is_test: bool = False) -> Path:
    """Standardized path builder: <root>/<year>/aoc<year>-<day><suffix>.txt"""
    root = get_data_root()
    suffix = "-test" if is_test else ""
    filename = f"aoc{year}-{day:02d}{suffix}.txt"

    p = root / str(year) / filename
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def download_input(year: int, day: int) -> Path:
    """Downloads input from AOC and saves to the .env defined root."""
    sess = os.getenv("AOC_SESSION")
    if not sess:
        raise RuntimeError("AOC_SESSION is not set in environment.")

    path = get_input_path(year, day, is_test=False)

    # Don't re-download if we already have it
    if path.exists(): return path

    url = f"{AOC_BASE}/{year}/day/{day}/input"
    r = requests.get(url, cookies={"session": sess}, timeout=30)
    r.raise_for_status()

    path.write_text(r.text.replace("\r\n", "\n").rstrip("\n") + "\n", encoding="utf-8")
    return path


def load_input(year: int, day: int, part: int = 1, is_test: bool = False):
    root = get_data_root()
    year_dir = Path(root) / str(year)
    search_patterns = []

    if is_test:
        # 1. Specific Part & Test (Matches 2024 Day 3/17 p01/p02)
        search_patterns.append(f"aoc{year}d{day:02d}p{part:02d}_test_input.txt")
        search_patterns.append(f"aoc{year}-{day:02d}-{part:02d}-test.txt")

        # 2. Year_DayDay_TestInput (Matches your 2021 files: aoc2021_1201_testinput.txt)
        # Note: 2021 used day + day again? i.e. 1201 for day 12.
        search_patterns.append(f"aoc{year}_{day:02d}01_testinput.txt")

        # 3. Standard Test variations (Matches 2025/2024: aoc2025-01-test.txt)
        search_patterns.append(f"aoc{year}-{day:02d}-test.txt")
        search_patterns.append(f"aoc{year}-{day:02d}-testinput.txt")
        search_patterns.append(f"aoc{year}d{day:02d}_test_input.txt")
        search_patterns.append(f"aoc{year}d{day:02d}_test.txt")
    else:
        # 1. Standard Input (Matches 2025/2024: aoc2025-01.txt)
        search_patterns.append(f"aoc{year}-{day:02d}.txt")
        search_patterns.append(f"aoc{year}-{day:02d}-input.txt")

        # 2. dXX_input (Matches 2024 Day 17: aoc2024d17_input.txt)
        search_patterns.append(f"aoc{year}d{day:02d}_input.txt")
        search_patterns.append(f"aoc{year}d{day:02d}.txt")

        # 3. Year_DayDay_input (Matches 2021: aoc2021_1201_input.txt)
        search_patterns.append(f"aoc{year}_{day:02d}01_input.txt")

    for pattern in search_patterns:
        path = year_dir / pattern
        if path.exists():
            return path.read_text(encoding="utf-8").splitlines()

    raise FileNotFoundError(f"Missing input: {year} Day {day} (Part: {part} Test: {is_test})")

def time_call(fn, *args, **kwargs):
    t0 = time.perf_counter()
    result = fn(*args, **kwargs)
    elapsed = (time.perf_counter() - t0) * 1000 # Convert to ms to match C#
    return result, elapsed