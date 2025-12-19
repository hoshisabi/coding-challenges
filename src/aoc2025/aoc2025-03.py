import sys

def get_data(fname):
    lines = None
    with open(fname) as f:
        lines = f.readlines()
    return lines

def solve_line(line):
    return 0

def solve(data):
    data_sum = 0
    for line in data:
        data_sum += solve_line(line)
    return data_sum

if __name__ == '__main__':
    # data, expected1, expected2 = get_data("aoc2025-03.txt"), 357, 357
    data, expected1, expected2 = get_data("aoc2025-03-test.txt"), 357, 357

    part1 = solve(data)
    part2 = solve(data)
    print(f"part 1: {part1}, match expected: {expected1 == part1}")
    print(f"part 2: {part2}, match expected: {expected2 == part2}")
