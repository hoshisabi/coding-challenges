def read_grid_from_file(filename):
    lines = []
    with open(filename, 'r') as file:
        lines.extend(line.strip() for line in file)
    return lines

def is_valid(grid, c, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == c

