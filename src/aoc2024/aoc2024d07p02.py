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
        return bool(helper(index + 1, int(str(current) + str(operands[index]))))

    # Start the recursion with the first operand
    return expected if helper(1, operands[0]) else 0


def solve_puzzle(filename):
    input_data = read_from_file(filename)
    return sum(
        find_expected_result_recursive(expected, operands)
        for expected, operands in input_data
    )


# Test data:
result = solve_puzzle("aoc2024d07_test_input.txt")
print(f"Sum of valid results in test data: {result}")
assert result == 11387, "Example did not match"

# Run the solution
result = solve_puzzle("aoc2024d07_input.txt")
print(f"Sum of valid results in real input: {result}")
