from aoc_shared.aoc_tools import load_input
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

def is_invalid(id, maxLength):
    if not maxLength:
        maxLength = len(id)
    for n in range(2, maxLength + 1):
        if is_invalid_pieces(id, n):
            return True
    return False

def count_invalid_for_range(left, right, stopat):
    count = sum(range_id for range_id in range(left, right + 1) if is_invalid(str(range_id), stopat))
    return count

def solve(data, maxLength):
    count = 0
    for line in data:
        idlist = line.strip().split(",")
        for id in idlist:
            if not id:
                continue
            else:
                left, right = id.split("-")
                if left and right:
                    count += count_invalid_for_range(int(left), int(right), maxLength)
    return count


if __name__ == '__main__':
    data = load_input(2025, 2, is_test=False)

    print("Day 2")
    part1 = solve(data, 2)
    print(f"part 1: {part1}")
    part2 = solve(data, None)
    print(f"part 2: {part2}")