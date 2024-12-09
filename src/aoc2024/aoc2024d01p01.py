from aoc2024d01_util import read_input_file

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    return sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

# Solve the puzzle with input from file
def solve_puzzle(filename):
    left_input, right_input = read_input_file(filename)
    return calculate_total_distance(left_input, right_input)

# Test data:
test_result = solve_puzzle("aoc2024d01_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 11, "Example did not match"

# Run the solution
total_distance = solve_puzzle("aoc2024d01_input.txt")
print(f"Total distance between location ID lists: {total_distance}")