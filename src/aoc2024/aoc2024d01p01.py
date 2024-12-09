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
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
test_result = calculate_total_distance([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
print(f"Solving for test input: {test_result}")

# Run the solution
input_filename = "aoc2024d01_input.txt"
total_distance = solve_puzzle(input_filename)
print(f"Total distance between location ID lists: {total_distance}")