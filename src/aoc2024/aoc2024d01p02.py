from aoc2024d01_util import read_input_file

def find_similarity_score(left_list, right_list):
    # Sort both lists
    return sum(x * right_list.count(x) for x in left_list)

# Solve the puzzle with input from file
def solve_puzzle(filename):
    left_input, right_input = read_input_file(filename)
    return find_similarity_score(left_input, right_input)

# Run on test data
test_result = solve_puzzle("aoc2024d01_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 31, "Example did not match"

# Run the solution
input_filename = "aoc2024d01_input.txt"
total_distance = solve_puzzle(input_filename)
print(f"Total distance between location ID lists: {total_distance}")