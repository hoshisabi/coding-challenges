def read_from_file(filename):
    walls = []
    current_pos = []
    max_x = -1
    max_y = -1
    facing = ""

    with open(filename, 'r') as file:
        for y, line in enumerate(file.readlines()):
            max_y = max(y, max_y)
            for x, obj in enumerate(line):
                max_x = max(y, max_x)
                if obj == "#":
                    walls += [(x,y)]
                elif obj in ("^", "<", ">", "v"):
                    current_pos = (x,y)
                    facing = obj
    return [walls, current_pos, facing, (max_x, max_y)]


def print_map(walls, current_pos, facing, max_coord, past_moves):
    new_map = ""

    for y in (range(1 + max_coord[1])):
        for x in (range(1 + max_coord[0])):
            if (x,y) in walls:
                new_map += "#"
            elif (x,y) == current_pos:
                new_map += facing
            elif (x,y) in past_moves:
                new_map += "X"
            else:
                new_map += "."
        new_map += "\n"
    return new_map

facing_deltas = {"^": (0, -1, ">"), ">": (1, 0, "v"), "v": (0, 1, "<"), "<": (-1, 0, "^")}


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

def solve_puzzle(filename):
    walls, current_pos, facing, max_coord = read_from_file(filename)
    past_moves = [current_pos]
    while facing != "":
        current_pos, facing, past_moves = move_guard(walls, current_pos, facing, max_coord, past_moves)
        #print(print_map(walls, current_pos, facing, max_coord, past_moves))
    return len(past_moves)


# Test data:
test_result = solve_puzzle("aoc2024d06_test_input.txt")
print(f"Guard visited distinct positions in test data: {test_result}")
assert test_result == 41, "Example did not match"

# Run the solution
total = solve_puzzle("aoc2024d06_input.txt")
print(f"Guard visited distinct positions in real input: {total}")
