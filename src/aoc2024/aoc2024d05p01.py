from aoc2024d05_util import *


def solve_puzzle(filename):
    comparisons, updates = read_from_file(filename)
    updates_valid = list(filter(lambda x: check(x, comparisons), updates))
    midpoints = list(map(midpoint, updates_valid))
    return sum(midpoints)


# Test data:
test_result = solve_puzzle("aoc2024d05_test_input.txt")
print(f"Total midpoints in valid test data: {test_result}")
assert test_result == 143, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d05_input.txt")
print(f"Total midpoints in valid real input: {total}")
