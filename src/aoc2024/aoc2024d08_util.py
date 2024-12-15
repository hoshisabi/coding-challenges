def read_map(file_name):
    antenna_map = {}
    max_x = -1
    max_y = -1
    with open(file_name, 'r') as file:
        for x, line in enumerate(list(line.strip()) for line in file.readlines()):
            max_x = max(max_x, x)
            for y, char in enumerate(line):
                max_y = max(max_y, y)
                if char.isalnum():
                    if char not in antenna_map:
                        antenna_map[char] = [(x, y)]
                    else:
                        antenna_map[char].append((x, y))
    return antenna_map, max_x, max_y

