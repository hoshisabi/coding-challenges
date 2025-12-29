from aoc2024d01_util import load_columns

def find_similarity_score(left_list, right_list):
    # Sort both lists
    return sum(x * right_list.count(x) for x in left_list)

# Solve the puzzle with input from file
def solve_puzzle(is_test):
    left_input, right_input = load_columns(2, is_test)
    return find_similarity_score(left_input, right_input)

# Run on test data
test_result = solve_puzzle(True)
print(f"Solving for test input: {test_result}")
assert test_result == 31, "Example did not match"

# Run the solution
total_distance = solve_puzzle(False)
print(f"Total distance between location ID lists: {total_distance}")