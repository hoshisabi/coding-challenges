def read_from_file(filename):
    presents = []
    with open(filename, 'r') as file:
        presents.extend(list(map(int, line.strip().split("x"))) for line in file)
    return presents


def solve_puzzle(filename):
    presents = read_from_file(filename)
    return sum(min(2 * l + 2 * w, 2 * l + 2 * h, 2 * w + 2 * h) + l * w * h for l, w, h in presents)

# Test data:
test_result = solve_puzzle("aoc2015d02_test_input.txt")
print(f"Total square feet in test data: {test_result}")
assert test_result == 34 + 14, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2015d02_input.txt")
print(f"Total square feet in real input: {total}")
