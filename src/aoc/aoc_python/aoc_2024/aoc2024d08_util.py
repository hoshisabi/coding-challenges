from aoc_shared.aoc_tools import load_input


def read_map(is_test):
    antenna_map = {}
    max_x = -1
    max_y = -1
    lines = load_input(2024, 8, 1, is_test)
    for x, line in enumerate(list(line.strip()) for line in lines):
        max_x = max(max_x, x)
        for y, char in enumerate(line):
            max_y = max(max_y, y)
            if char.isalnum():
                if char not in antenna_map:
                    antenna_map[char] = [(x, y)]
                else:
                    antenna_map[char].append((x, y))
    return antenna_map, max_x, max_y

