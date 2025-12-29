import os, pathlib, time, requests

AOC_BASE = "https://adventofcode.com"

def aoc_input_path(year: int, day: int, test: bool = False) -> pathlib.Path:
    p = pathlib.Path("inputs") / f"{year}" / f"day{day:02d}{'.test' if test else ''}.txt"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def download_input(year: int, day: int) -> pathlib.Path:
    sess = os.getenv("AOC_SESSION")
    if not sess:
        raise RuntimeError("AOC_SESSION is not set. Set it in your environment.")
    url = f"{AOC_BASE}/{year}/day/{day}/input"
    cookies = {"session": sess}
    r = requests.get(url, cookies=cookies, timeout=30)
    r.raise_for_status()
    path = aoc_input_path(year, day, test=False)
    path.write_text(r.text.replace("\r\n", "\n").rstrip("\n") + "\n", encoding="utf-8")
    return path

def read_lines(path: pathlib.Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()

def time_call(fn, *args, **kwargs):
    t0 = time.perf_counter()
    result = fn(*args, **kwargs)
    elapsed = time.perf_counter() - t0
    return result, elapsed