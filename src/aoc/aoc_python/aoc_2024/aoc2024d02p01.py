from aoc2024d02_util import read_input_file, verify_report

# Solve the puzzle with input from file
def solve_puzzle(filename):
    reports = read_input_file(filename)
    return sum(verify_report(report) for report in reports)

# Test data:
test_result = solve_puzzle(True)
print(f"Solving for test input: {test_result}")
assert test_result == 2, "Example did not match"

# Run the solution
total_distance = solve_puzzle(False)
print(f"Total distance between location ID lists: {total_distance}")
