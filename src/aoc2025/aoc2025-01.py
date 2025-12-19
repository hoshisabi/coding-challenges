import sys

def get_data(fname):
    lines = None
    with open(fname) as f:
        lines = f.readlines()
    return lines


def solve(data):
    dial_pos = 50
    part1_zeros = 0
    part2_zeros = 0

    for instruction in data:
        if not instruction:
            continue
        
        direction = instruction[0]
        distance = int(instruction[1:])
        if direction == "L":
            part2_zeros += distance // 100
            if dial_pos != 0 and (distance % 100) >= dial_pos:
                part2_zeros += 1
            dial_pos = (dial_pos - distance) % 100
        else:
            part2_zeros += (dial_pos + distance) // 100
            dial_pos = (dial_pos + distance) % 100

        if dial_pos == 0:
            part1_zeros += 1

    return part1_zeros, part2_zeros, dial_pos

if __name__ == '__main__':
    data = get_data("aoc2025-01.txt")
    # data = get_data("aoc2025-01-test.txt")
    # data = ["L50"]
    print(solve(data))

    # Expected:
    #   part 1:	1195
    #   part 2:	6770