from aoc2024d07_util import *

def find_expected_result_recursive(expected, operands):
    def helper(index, current):
        if index == len(operands):
            return current == expected
        # Try addition
        if helper(index + 1, current + operands[index]):
            return True
        # Try multiplication
        if helper(index + 1, current * operands[index]):
            return True
        # Try concatenation
        if helper(index + 1, int(str(current) + str(operands[index]))):
            return True
        return False

    # Start the recursion with the first operand
    if helper(1, operands[0]):
        return expected
    else:
        return 0


def solve_puzzle(filename):
    input_data = read_from_file(filename)
    total = 0
    for expected, operands in input_data:
        result = find_expected_result_recursive(expected, operands)
        total += result
    return total


# Test data:
test_result = solve_puzzle("aoc2024d07_test_input.txt")
print(f"Sum of valid results in test data: {test_result}")
assert test_result == 11387, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d07_input.txt")
print(f"Sum of valid results in real input: {total}")
