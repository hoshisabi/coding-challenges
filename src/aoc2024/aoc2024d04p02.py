from aoc2024d04_util import *

def read_grid_from_file(filename):
    lines = []
    with open(filename, 'r') as file:
        lines.extend(line.strip() for line in file)
    return lines

def is_valid(grid, c, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c


word_cross_directions = [
    (0, 1, 1, 0, 0, -1, -1, 0),  # m = right, m = down
    (0, -1, 1, 0, 0, 1, -1, 0),  # m = left, m = down
    (0, 1, -1, 0, 0, -1, 1, 0),  # m = right, m = up
    (0, -1, -1, 0, 0, 1, 1, 0),  # m = left, m = up
    (1, -1, 1, 1, -1, 1, -1, -1),  # m = left-down diagonal, m = right-down diagonal
    (1, -1, -1, -1, -1, 1, 1, 1),  # m = left-down diagonal, m = left-up diagonal
    (1, 1, -1, 1, -1, -1, 1, -1),  # m = right-down diagonal, m = right-up diagonal
    (1, 1, -1, -1, -1, -1, 1, 1),  # m = right-down diagonal, m = left-up diagonal
]


# Solve the puzzle with input from file
def solve_puzzle(filename):  # sourcery skip: use-itertools-product
    grid = read_grid_from_file(filename)
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if is_valid(grid, 'A', x, y):
                count = check_cross(count, grid)
    return count


def check_cross(count, grid):
    for m1x, m1y, m2x, m2y, s1x, s1y, s2x, s2y in word_cross_directions:
        if is_valid(grid, 'M', m1x, m1y) and is_valid(grid, 'S', s1x, s2y) and is_valid(grid, 'M', m2x,
                                                                                        m2y) and is_valid(
                grid, 'S', s2x, s2y):
            count += 1
    return count


# Test data:
test_result = solve_puzzle("aoc2024d04_test_input.txt")
print(f"Count of X-MAS in test data: {test_result}")
assert test_result == 9, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d04_input.txt")
print(f"Total X-MAS found in real input: {total}")
