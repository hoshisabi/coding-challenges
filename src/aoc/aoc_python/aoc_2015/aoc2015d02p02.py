from aoc_shared.aoc_tools import load_input


def read_from_file(is_test):
    presents = load_input(2015, 2, 2, is_test)
    presents.extend(list(map(int, line.strip().split("x"))) for line in file)
    return presents


def solve_puzzle(is_test):
    presents = []
    lines = load_input(2015, 2, 2, is_test)
    presents.extend(list(map(int, line.strip().split("x"))) for line in lines)
    return sum(min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h) + l * w * h for l, w, h in presents)

# Test data:
test_result = solve_puzzle(True)
print(f"Total square feet in test data: {test_result}")
assert test_result == 34 + 14, "Example did not match"

# Run the solution
total = solve_puzzle(False)
print(f"Total square feet in real input: {total}")
