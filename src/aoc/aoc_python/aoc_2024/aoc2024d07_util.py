from aoc_shared.aoc_tools import load_input


def read_from_file(is_test):
    lines = load_input(2024, 7, 1, is_test)
    equations = [
        (int(result), list(map(int, operands.strip().split())))
        for line in lines
        for result, operands in [line.strip().split(':')]
    ]
    return equations
