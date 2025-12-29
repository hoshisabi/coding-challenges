from aoc_shared.aoc_tools import load_input

def solve_puzzle(is_test):
    instructions = load_input(2015, 1, 1, is_test)[0].strip()
    return instructions.count("(") - instructions.count(")")

# Test data:
test_result = solve_puzzle(True)
print(f"Final floor in test data: {test_result}")
assert test_result == -3, "Example did not match"

# Run the solution
total = solve_puzzle(False)
print(f"Final floor in real input: {total}")
