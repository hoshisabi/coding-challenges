from aoc2024d01_util import load_columns

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    return sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

# Solve the puzzle with input from file
def solve_puzzle(is_test):
    left_input, right_input = load_columns(1, is_test)
    return calculate_total_distance(left_input, right_input)


# Test data:
test_result = solve_puzzle(True)
print(f"Solving for test input: {test_result}")
assert test_result == 11, "Example did not match"

# Run the solution
total_distance = solve_puzzle(False)
print(f"Total distance between location ID lists: {total_distance}")