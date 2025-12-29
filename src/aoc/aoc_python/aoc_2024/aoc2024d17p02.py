from aoc2024d17_util import *

def execute_program(program, reg_a, reg_b, reg_c):
    halt = False
    out = []
    ip = 0
    while not halt:
        halt, ip, reg_a, reg_b, reg_c, out = execute_instruction(program, ip, reg_a, reg_b, reg_c, out)
        if out and out != program[: len(out)]:
            break
    return out


def solve_puzzle(is_test):
    # Pass all 4 arguments: Year, Day, Part, is_test
    # Day 17 Part 2 test data is specifically in the p02 file
    reg_a, reg_b, reg_c, program = read_file_modern(2, is_test)

    # Start at len(program) - 1 to match the last index of the program
    return solve(0, len(program) - 1, program, reg_b, reg_c)


def solve(n, d, program, reg_b=0, reg_c=0):
    res = [1e20]  # Sentinel value for failure
    if d == -1:
        return n

    for i in range(8):
        # We build the number from the most significant octal digit down
        nn = n + i * (8 ** d)
        out = execute_program(program, nn, reg_b, reg_c)

        # Ensure output is long enough and the specific digit matches
        if len(out) == len(program) and out[d] == program[d]:
            val = solve(nn, d - 1, program, reg_b, reg_c)
            res.append(val)

    return min(res)

# Test data:
result = solve_puzzle(True)
print(f"Output of program with test input: {result}")
assert result == 117440, f"Example did not match ({result} vs expected 117440)"

# Run the solution
result = solve_puzzle(False)
print(f"Output of program with real input: {result}")
