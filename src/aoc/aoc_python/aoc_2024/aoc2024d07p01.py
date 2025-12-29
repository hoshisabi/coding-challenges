from aoc2024d07_util import *


def find_expected_result_recursive(expected, operands):
    if not operands:  # Check if operands are empty or null
        return 0

    def helper(index, current):
        if index == len(operands):
            return current == expected
        # Try addition
        if helper(index + 1, current + operands[index]):
            return True
        # Try multiplication
        return helper(index + 1, current * operands[index])

    # Start the recursion with the first operand
    return expected if helper(1, operands[0]) else 0


def solve_puzzle(is_test):
    input_data = read_from_file(is_test)
    return sum(
        find_expected_result_recursive(expected, operands)
        for expected, operands in input_data
    )


# Test data:
result = solve_puzzle(True)
print(f"Sum of valid results in test data: {result}")
assert result == 3749, "Example did not match"

# Run the solution
result = solve_puzzle(False)
print(f"Sum of valid results in real input: {result}")
