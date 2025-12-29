from aoc2024d08_util import *

def solve_puzzle(is_test):
    antenna_map, max_x, max_y = read_map(is_test)
    print(antenna_map, max_x, max_y)
    return 10

# Test data:
result = solve_puzzle(True)
print(f"Sum of valid results in test data: {result}")
assert result == 14, "Example did not match"

# Run the solution
result = solve_puzzle(False)
print(f"Sum of valid results in real input: {result}")
