
def check(line, comparisons):
    for compare in comparisons:
        if compare[0] in line and compare[1] in line:
            left = line.index(compare[0])
            right = line.index(compare[1])
            if left > right:
                return False
    return True


def midpoint(line):
    mid_index = len(line) // 2
    return int(line[mid_index])


def read_from_file(filename):
    comparisons = []
    updates = []
    in_updates = False

    with open(filename, 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped == "":
                in_updates = True
            elif in_updates:
                updates += [stripped.split(",")]
            else:
                comparisons += [stripped.split("|")]
    return [comparisons, updates]

