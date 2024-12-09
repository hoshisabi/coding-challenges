from aoc2024d04_util import *


def read_grid_from_file(filename):
    lines = []
    with open(filename, 'r') as file:
        lines.extend(line.strip() for line in file)
    return lines


def is_valid(grid, c, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c


word_cross_directions = [
    (-1, -1, -1, 1, 1, -1, 1, 1), # M up-left, M up-right, S down-left, S down-right
    (-1, -1, 1, -1, -1, 1, 1, 1), # M up-left, M down-left, S up-right, S down-right
    (-1, 1, 1, 1, 1, -1, -1, -1), # M up-right, M down-right, S down-left, S up-left
    (1, -1, 1, 1, -1, -1, -1, 1), # M down-left, M down-right, S up-left, S up-right
]

# Solve the puzzle with input from file
def solve_puzzle(filename):  # sourcery skip: use-itertools-product
    grid = read_grid_from_file(filename)
    a_indices = [(x, y) for x, row in enumerate(grid) for y, char in enumerate(row) if char == 'A']
    count = 0
    for (x, y) in a_indices:
        for c in word_cross_directions:
            if (is_valid(grid, 'M', x + c[0], y + c[1]) and
                    is_valid(grid, 'M', x + c[2], y + c[3]) and
                    is_valid(grid, 'S', x + c[4], y + c[5]) and
                    is_valid(grid, 'S', x + c[6], y + c[7])):
                count += 1
    return count

# Test data:
test_result = solve_puzzle("aoc2024d04_test_input.txt")
print(f"Count of X-MAS in test data: {test_result}")
assert test_result == 9, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d04_input.txt")
print(f"Total X-MAS found in real input: {total}")
