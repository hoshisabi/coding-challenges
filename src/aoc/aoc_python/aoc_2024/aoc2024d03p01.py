from aoc_shared.aoc_tools import load_input
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
def solve_puzzle(lines):
    numbers = find_valid_numbers(lines)
    return execute_instruction(numbers)

# Test data:
lines = load_input(2024, 3, part = 1, is_test = True)
test_result = solve_puzzle(lines)
print(f"Solving for test input: {test_result}")
assert test_result == 161, "Example did not match"

# Run the solution
lines = load_input(2024, 3, part = 1, is_test = False)
total = solve_puzzle(lines)
print(f"Total of mul commands: {total}")