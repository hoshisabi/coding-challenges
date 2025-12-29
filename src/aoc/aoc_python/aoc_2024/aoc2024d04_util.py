from aoc_shared.aoc_tools import load_input

def read_grid_from_file(is_test):
    lines = load_input(2024, 4, 1, is_test)
    return list(line.strip() for line in lines)

def is_valid(grid, c, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c

