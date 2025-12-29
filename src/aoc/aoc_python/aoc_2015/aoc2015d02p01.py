from aoc_shared.aoc_tools import load_input


def read_from_file(filename):
    presents = []
    lines = load_input(2015, 2, 1, filename)
    presents.extend(list(map(int, line.strip().split("x"))) for line in lines)
    return presents


def solve_puzzle(filename):
    presents = read_from_file(filename)
    return sum(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l, w, h in presents)

# Test data:
test_result = solve_puzzle(True)
print(f"Total square feet in test data: {test_result}")
assert test_result == 58 + 43, "Example did not match"

# Run the solution
total = solve_puzzle(False)
print(f"Total square feet in real input: {total}")
