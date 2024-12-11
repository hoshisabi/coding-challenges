import time
from aoc2024d06_util import *


def move_guard(walls, current_pos, facing, max_coord, visited):
    delta = facing_deltas[facing]
    possible = (current_pos[0] + delta[0], current_pos[1] + delta[1])
    if possible in walls:
        facing = delta[2]
    elif possible[0] > max_coord[0] or possible[1] > max_coord[1] or possible[0] < 0 or possible[1] < 0:
        facing = "?"
        current_pos = (-1, -1)
    elif (possible[0], possible[1], facing) in visited:
        facing = "X"
    else:
        current_pos = possible
        visited += [(current_pos[0], current_pos[1], facing)]
    return [current_pos, facing, visited]


def get_visits(current_pos, facing, initial_current_pos, initial_facing, max_coord, max_moves, new_walls, walls):
    visited = []
    moves = 0
    while moves < max_moves:
        moves += 1
        current_pos, facing, visited = move_guard(walls, current_pos, facing, max_coord, visited)
        if facing in ["X", "?"]:
            break
    return facing, visited


def get_all_moves(walls, current_pos, facing, max_coord):
    new_walls = []
    initial_current_pos = current_pos
    initial_facing = facing
    max_moves = 10000
    facing, original_visits = get_visits(current_pos, facing, initial_current_pos, initial_facing,
                                         max_coord, max_moves, new_walls, walls)

    possible_walls = []
    for visit in original_visits:
        if (visit[0], visit[1]) not in possible_walls:
            possible_walls += [(visit[0], visit[1])]

    for possible_new_wall in possible_walls:
        x = possible_new_wall[0]
        y = possible_new_wall[1]
        facing = initial_facing
        current_pos = initial_current_pos
        if (x, y) != current_pos and (x, y) not in walls:
            facing, visited = get_visits(current_pos, facing, initial_current_pos, initial_facing,
                                         max_coord, max_moves, new_walls, walls + [(x, y)])
            if facing == "X" and possible_new_wall not in new_walls:
                new_walls += [possible_new_wall]
    return new_walls


def solve_puzzle(filename):
    walls, current_pos, facing, max_coord = read_from_file(filename)
    new_walls = get_all_moves(walls, current_pos, facing, max_coord)
    print(new_walls)
    return len(new_walls)


# Test data:
start_time = time.time()
test_result = solve_puzzle("aoc2024d06_test_input.txt")
execution_time = start_time - time.time()
print(f"Number of teleported obstacles that cause circuit in test data: {test_result}, execution_time={execution_time}")
assert test_result == 6, "Example did not match"

# Run the solution
start_time = time.time()
total = solve_puzzle("aoc2024d06_input.txt")
execution_time = start_time - time.time()
print(f"Number of teleported obstacles that cause circuit in real input: {total}, execution_time={execution_time}")
