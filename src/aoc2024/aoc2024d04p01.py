from aoc2024d04_util import read_grid_from_file

def is_valid(grid, c, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c

def find_word(grid, word, start_x, start_y, delta_x, delta_y):
    x, y = start_x, start_y
    for c in word:
        if not is_valid(grid, c, x, y):
            return False
        x += delta_x
        y += delta_y
    return True

directions = [
    (0, 1), # right
    (0, -1), # left
    (1, 0), # down
    (-1, 0), # up
    (1, 1), # right-down diagonal
    (1, -1), # left-down diagonal
    (-1, 1), # right-up diagonal
    (-1, -1) # left-up diagonal
]

# Solve the puzzle with input from file
def solve_puzzle(filename):
    grid = read_grid_from_file(filename)
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for delta_x, delta_y in directions:
                if find_word(grid, "XMAS",x, y, delta_x, delta_y):
                    count += 1
    return count

# Test data:
test_result = solve_puzzle("aoc2024d04_test_input.txt")
print(f"Count of XMAS in test data: {test_result}")
assert test_result == 18, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d04_input.txt")
print(f"Total XMAS found in real input: {total}")