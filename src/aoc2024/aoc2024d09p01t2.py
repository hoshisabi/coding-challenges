from aoc2024d09_util import *

def get_checksum(block_map):
    return sum(
        address * block
        for address, block in enumerate(block_map)
        if block is not None
    )

def solve_puzzle(file_name):
    block_map = read_file(file_name)
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
result = solve_puzzle("aoc2024d09_test_input.txt")
print(f"Sum of valid results in test data: {result}")
assert result == 1928, "Example did not match"

# Run the solution
result = solve_puzzle("aoc2024d09_input.txt")
print(f"Sum of valid results in real input: {result}")
