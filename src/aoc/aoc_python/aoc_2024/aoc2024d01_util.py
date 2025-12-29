from aoc_shared.aoc_tools import load_input

def load_columns(part = 1, is_test: bool = False):
    """Specific helper for Day 1 style inputs with two integer columns."""
    lines = load_input(2024, 1, part, is_test)
    left_list = []
    right_list = []

    for line in lines:
        if not line.strip(): continue  # Skip empty lines
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    return left_list, right_list
