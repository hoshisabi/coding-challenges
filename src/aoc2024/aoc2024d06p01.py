from aoc2024d06_util import *

def move_guard(walls, current_pos, facing, max_coord, past_moves):
    delta = facing_deltas[facing]
    possible = (current_pos[0] + delta[0], current_pos[1] + delta[1])
    if possible in walls:
        facing = delta[2]
    elif possible[0] > max_coord[0] or possible[1] > max_coord[1] or possible[0] < 0 or possible[1] < 0:
        facing = ""
        current_pos = (-1, -1)
    else:
        current_pos = possible
        if current_pos not in past_moves:
            past_moves += [current_pos]
    return [current_pos, facing, past_moves]

def get_all_moves(walls, current_pos, facing, max_coord):
    past_moves = [current_pos]
    while facing != "":
        current_pos, facing, past_moves = move_guard(walls, current_pos, facing, max_coord, past_moves)
    return past_moves

def solve_puzzle(filename):
    walls, current_pos, facing, max_coord = read_from_file(filename)
    past_moves = get_all_moves(walls, current_pos, facing, max_coord)
    return len(past_moves)

# Test data:
test_result = solve_puzzle("aoc2024d06_test_input.txt")
print(f"Guard visited distinct positions in test data: {test_result}")
assert test_result == 41, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d06_input.txt")
print(f"Guard visited distinct positions in real input: {total}")
