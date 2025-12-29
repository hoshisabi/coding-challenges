from aoc2024d17_util import *

def solve_puzzle(is_test):
    halt = False
    reg_a, reg_b, reg_c, program = read_file_modern(1, is_test)
    instruction_pointer = 0
    out = []
    while not halt:
        halt, instruction_pointer, reg_a, reg_b, reg_c, out = execute_instruction(program, instruction_pointer, reg_a, reg_b, reg_c, out)
    return ",".join(map(str, out))

    # Test data:


result = solve_puzzle(True)
print(f"Output of program with test input: {result}")
assert result == "4,6,3,5,6,3,5,2,1,0", "Example did not match"

# Run the solution
result = solve_puzzle(False)
print(f"Output of program with real input: {result}")
