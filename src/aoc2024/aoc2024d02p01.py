from aoc2024d02_util import *


# Solve the puzzle with input from file
def solve_puzzle(filename):
    reports = read_input_file(filename)
    return sum(verify_report(report) for report in reports)


# Test data:
test_result = solve_puzzle("aoc2024d02_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 2, "Example did not match"

# Run the solution
total_distance = solve_puzzle("aoc2024d02_input.txt")
print(f"Total distance between location ID lists: {total_distance}")
