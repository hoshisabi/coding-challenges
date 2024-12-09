from aoc2024d02_util import *
from itertools import chain

def damper_output(report):
    return [list(chain(report[:i], report[i+1:])) for i in range(len(report))]

def verify_with_damper(report):
    damper = damper_output(report)
    return any(verify_report(x) for x in damper)

# Solve the puzzle with input from file
def solve_puzzle(filename):
    reports = read_input_file(filename)
    return sum(verify_with_damper(report) for report in reports)


# Test data:
test_result = solve_puzzle("aoc2024d02_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 4, "Example did not match"

# Run the solution
total_distance = solve_puzzle("aoc2024d02_input.txt")
print(f"Total distance between location ID lists: {total_distance}")
