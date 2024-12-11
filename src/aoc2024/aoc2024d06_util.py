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

