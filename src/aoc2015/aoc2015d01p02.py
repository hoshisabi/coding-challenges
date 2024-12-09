def read_from_file(filename):
    instructions = ""
    with open(filename, 'r') as file:
        for line in file:
            instructions += line.strip()
    return instructions


def solve_puzzle(filename):
    instructions = read_from_file(filename)
    floor = 0
    for pos, c in enumerate(instructions):
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1
        if floor < 0:
            return pos + 1
    return -1


# Test data:
test_result = solve_puzzle("aoc2015d01p02_test_input.txt")
print(f"Final floor in test data: {test_result}")
assert test_result == 5, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2015d01_input.txt")
print(f"Final floor in real input: {total}")
