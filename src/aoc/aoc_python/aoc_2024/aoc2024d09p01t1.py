from aoc_shared.aoc_tools import load_input


def add_file_at_address(disk_map, file_id, size, address):
    # print("afaa", disk_map, file_id, size, address)
    for i in range(address, address + size):
        disk_map[i] = file_id


def read_file(is_test):
    disk_map = {}
    disk_string= ""
    lines = load_input(2024, 9, 1, is_test)
    for line in lines:
        disk_string += line.strip()

    isfile = True
    file_id = 0
    address = 0
    for c in range(len(disk_string)):
        size = int(disk_string[c])
        if isfile:
            add_file_at_address(disk_map, file_id, size, address)
            file_id += 1
        address += size
        isfile = not isfile

    return disk_map, address, file_id

def get_disk_map_string(disk_map, max_loc):
    keys = disk_map.keys()
    return "".join(str(disk_map[i]) if i in keys else "." for i in range(max_loc+1))

def get_checksum(disk_map):
    return sum(disk_map[i] * i for i in range(len(disk_map)))


def is_compact(disk_map, max_loc):
    return all(i in disk_map.keys() for i in range(max_loc + 1))


def get_free_space_loc(disk_map, max_loc):
    filled_locs = disk_map.keys()
    return next(
        (i for i in range(max_loc) if i not in filled_locs),
        max_loc + 1,
    )


def move_file_id(file_id, disk_map, max_loc):
    locs = []
    for loc in disk_map.keys():
        if disk_map[loc] == file_id:
            locs += {loc}

    for loc in locs:
        new_loc = get_free_space_loc(disk_map, max_loc)
        disk_map.pop(loc)
        disk_map[new_loc] = file_id

    max_loc = max(disk_map.keys())
    return disk_map, max_loc


def solve_puzzle(is_test):
    disk_map, max_loc, num_files = read_file(is_test)

    for i in range(num_files - 1, 0, -1):
        if is_compact(disk_map, max_loc):
            print("compact")
            break
        else:
            # print(i, max_loc, "disk_map   before: ", get_disk_map_string(disk_map, max_loc))
            print("Compacting file_id ", i)
            disk_map, max_loc = move_file_id(i, disk_map, max_loc)
            # print(i, max_loc, "disk_map after : ", get_disk_map_string(disk_map, max_loc))

    return get_checksum(disk_map)


# Test data:
result = solve_puzzle(True)
print(f"Sum of valid results in test data: {result}")
assert result == 1928, "Example did not match"

# Run the solution
result = solve_puzzle(False)
print(f"Sum of valid results in real input: {result}")
