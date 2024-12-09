from aoc2024d01_util import read_input_file

def find_similarity_score(left_list, right_list):
    # Sort both lists
    return sum(x * right_list.count(x) for x in left_list)

# Solve the puzzle with input from file
def solve_puzzle(filename):
    left_input, right_input = read_input_file(filename)
    return find_similarity_score(left_input, right_input)

# Run on test data
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
test_result = find_similarity_score([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])
print(f"Solving for test input: {test_result}")

# Run the solution
input_filename = "aoc2024d01_input.txt"
total_distance = solve_puzzle(input_filename)
print(f"Total distance between location ID lists: {total_distance}")