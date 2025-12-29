from aoc_shared.aoc_tools import load_input

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


if __name__ == "__main__":
    # Use the helper to find the file via .env
    data = load_input(2025, 1, is_test=True)
    result = solve(data)
    print("Day 1")
    print(f"Result: {result}")
