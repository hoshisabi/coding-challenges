def read_from_file(filename):
    presents = []
    with open(filename, 'r') as file:
        presents.extend(list(map(int, line.strip().split("x"))) for line in file)
    return presents


def solve_puzzle(filename):
    presents = read_from_file(filename)
    return sum(2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l) for l, w, h in presents)

# Test data:
test_result = solve_puzzle("aoc2015d02_test_input.txt")
print(f"Total square feet in test data: {test_result}")
assert test_result == 58 + 43, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2015d02_input.txt")
print(f"Total square feet in real input: {total}")
