from aoc2024d03_util import read_input_file
import re


def find_valid_numbers(lines):
    mul_string = r"mul\((\d+),(\d+)\)"
    mul_pattern = re.compile(mul_string)
    do_string = r"do\(\)"
    do_pattern = re.compile(do_string)
    dont_string = r"don't\(\)"
    dont_pattern = re.compile(dont_string)
    numbers = []
    enabled = True

    for line in lines:
        tokens = re.findall(f"mul\(\d+,\d+\)|{do_string}|{dont_string}", line)

        for token in tokens:
            if do_pattern.match(token):
                enabled = True
            elif dont_pattern.match(token):
                enabled = False
            elif enabled and mul_pattern.match(token):
                operands = mul_pattern.findall(token)[0]
                num1, num2 = map(int, operands)
                numbers.append([num1, num2])

    return numbers


def execute_instruction(pairs):
    return sum(x * y for x, y in pairs)


# Solve the puzzle with input from file
def solve_puzzle(filename):
    lines = read_input_file(filename)
    numbers = find_valid_numbers(lines)
    return execute_instruction(numbers)


# Test data:
test_result = solve_puzzle("aoc2024d03p02_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 48, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d03_input.txt")
print(f"Total of mul commands: {total}")
