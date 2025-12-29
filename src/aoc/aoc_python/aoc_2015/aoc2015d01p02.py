from aoc_shared.aoc_tools import load_input

def solve_puzzle(is_test):
    instructions = load_input(2015, 1, 2, is_test)[0].strip()
    instruction = instructions[0].strip()
    floor = 0
    for pos, c in enumerate(instruction):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            return pos + 1
    return -1


# Test data:
test_result = solve_puzzle(True)
print(f"Final floor in test data: {test_result}")
assert test_result == 5, "Example did not match"

# Run the solution
total = solve_puzzle(False)
print(f"Final floor in real input: {total}")
