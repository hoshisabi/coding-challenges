from aoc2024d17_util import *

def solve_puzzle(filename):
    halt = False
    reg_a, reg_b, reg_c, program = read_file(filename)
    instruction_pointer = 0
    out = []
    while not halt:
        halt, instruction_pointer, reg_a, reg_b, reg_c, out = execute_instruction(program, instruction_pointer, reg_a, reg_b, reg_c, out)
    return ",".join(map(str, out))

    # Test data:


result = solve_puzzle("aoc2024d17p01_test_input.txt")
print(f"Output of program with test input: {result}")
assert result == "4,6,3,5,6,3,5,2,1,0", "Example did not match"

# Run the solution
result = solve_puzzle("aoc2024d17_input.txt")
print(f"Output of program with real input: {result}")
