from aoc2024d03_util import read_input_file
import re

def find_valid_numbers(lines):
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    numbers = []
    for line in lines:
        matches = pattern.findall(line)
        numbers.extend([list(map(int, match)) for match in matches])
    return numbers

def execute_instruction(pairs):
    return sum(x * y for x, y in pairs)

# Solve the puzzle with input from file
def solve_puzzle(filename):
    lines = read_input_file(filename)
    numbers = find_valid_numbers(lines)
    return execute_instruction(numbers)

# Test data:
test_result = solve_puzzle("aoc2024d03p01_test_input.txt")
print(f"Solving for test input: {test_result}")
assert test_result == 161, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d03_input.txt")
print(f"Total of mul commands: {total}")