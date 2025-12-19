import sys

def get_data(fname):
    lines = None
    with open(fname) as f:
        lines = f.readlines()
    return lines

def is_invalid_pieces(id, pieces):
    # only check when the string is divisible by this amount
    if len(id) % pieces != 0:
        return False

    # Check to see if the string is made up only of the fragment fully repeated
    frag_len = len(id) // pieces
    id_frag = id[0:frag_len]
    id_repeat = id_frag * pieces
    if id == id_repeat:
        return True
    return False


def is_invalid(id):
    for n in range(2, len(id) + 1):
        if is_invalid_pieces(id, n):
            return True
    return False

def count_invalid_for_range(left, right):
    count = sum(range_id for range_id in range(left, right + 1) if is_invalid(str(range_id)))
    return count

def solve(data, stopat):
    count = 0
    for line in data:
        idlist = line.strip().split(",")
        for id in idlist:
            if not id:
                continue
            else:
                left, right = id.split("-")
                if left and right:
                    count += count_invalid_for_range(int(left), int(right))
    return count


if __name__ == '__main__':
    # data, expected1, expected2 = get_data("aoc2025-02.txt"), 23701357374, 34284458938
    data, expected1, expected2 = get_data("aoc2025-02-test.txt"), 1227775554, 4174379265

    part1 = solve(data, 2)
    part2 = solve(data, None)
    print(f"part 1: {part1}, match expected: {expected1 == part1}")
    print(f"part 2: {part2}, match expected: {expected2 == part2}")
