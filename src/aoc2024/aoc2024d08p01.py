from aoc2024d08_util import *

def solve_puzzle(file_name):
    antenna_map, max_x, max_y = read_map(file_name)
    print(antenna_map, max_x, max_y)
    return 10

# Test data:
result = solve_puzzle("aoc2024d08_test_input.txt")
print(f"Sum of valid results in test data: {result}")
assert result == 14, "Example did not match"

# Run the solution
result = solve_puzzle("aoc2024d08_input.txt")
print(f"Sum of valid results in real input: {result}")
