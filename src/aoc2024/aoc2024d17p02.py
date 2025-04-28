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

def solve(n, d, program, reg_b=0, reg_c=0):
    res = [1e20]
    if d == -1:
        return n
    for i in range(8):
        nn = n + i * 8 ** d
        out = execute_program(program, nn, reg_b, reg_c)
        if len(out) != len(program):
            continue
        if out[d] == program[d]:
            res.append(solve(nn, d-1))
    return min(res)

def solve_puzzle(filename):
    reg_a, reg_b, reg_c, program = read_file(filename)
    return solve(0, len(program), program, reg_b, reg_c)


# Test data:
    # Test data:
result = solve_puzzle("aoc2024d17p02_test_input.txt")
print(f"Output of program with test input: {result}")
assert result == 117440, "Example did not match"

# Run the solution
result = solve_puzzle("aoc2024d17_input.txt")
print(f"Output of program with real input: {result}")
