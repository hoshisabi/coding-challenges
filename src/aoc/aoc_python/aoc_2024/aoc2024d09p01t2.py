from aoc2024d09_util import *


def solve_puzzle(is_test):
    block_map = load_input(2024, 9, 1, is_test)
    left_pointer = 0
    right_pointer = len(block_map) - 1
    while left_pointer < right_pointer:
        # look for free space
        if block_map[left_pointer] is not None:
            left_pointer += 1
            continue

        print(left_pointer, right_pointer, len(block_map))
        block_map[left_pointer] = block_map.pop()
        right_pointer -= 1


    return get_checksum(block_map)


# Test data:
result = solve_puzzle(True)
print(f"Sum of valid results in test data: {result}")
assert result == 1928, "Example did not match"

# Run the solution
result = solve_puzzle(False)
print(f"Sum of valid results in real input: {result}")
