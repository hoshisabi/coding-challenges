from aoc2024d05_util import *
from functools import cmp_to_key

def compare(comparisons, left, right):
    for comparison in comparisons:
        if comparison[0] == left and comparison[1] == right:
            return -1
        elif comparison[0] == right and comparison[1] == left:
            return 1
    return 0


def solve_puzzle(is_test):
    comparisons, updates = read_from_file(is_test)
    unsorted_lists = [inner_list for inner_list in updates if not check(inner_list, comparisons)]
    sorted_updates = []
    for update in unsorted_lists:
        sorted_update = sorted(update, key=cmp_to_key(lambda left, right: compare(comparisons, left, right)))
        sorted_updates.append(sorted_update)
    midpoints = list(map(midpoint, sorted_updates))
    return sum(midpoints)

# Test data:
test_result = solve_puzzle(True)
print(f"Total midpoints in valid test data: {test_result}")
assert test_result == 123, "Example did not match"

# Run the solution
total = solve_puzzle(False)
print(f"Total midpoints in valid real input: {total}")
