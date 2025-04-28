from itertools import batched

def disk_map_to_string(disk_map):
    return "".join(f"[{block}]" if block is not None else "[.]" for block in disk_map)

def read_file(filename):
    block_map = []

    # we only read the first line, if there are multiple.
    # it should only be one line
    with open(filename, 'r') as file:
        disk_string = file.readline().strip()

    for file_id, pair in enumerate(batched(disk_string, 2)):
        f, s = 0, 0
        if len(pair) == 2:
            f, s = map(int, pair)
        else:
            f = int(pair[0])

        for _ in range(f):
            block_map += [file_id]

        for _ in range(s):
            block_map += [ None ]

    return block_map

def get_checksum(block_map):
    return sum(
        address * block
        for address, block in enumerate(block_map)
        if block is not None
    )
