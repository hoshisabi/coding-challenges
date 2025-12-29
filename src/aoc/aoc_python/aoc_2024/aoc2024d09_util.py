from itertools import batched

from aoc_shared.aoc_tools import load_input


def disk_map_to_string(disk_map):
    return "".join(f"[{block}]" if block is not None else "[.]" for block in disk_map)


def read_file(is_test):
    block_map = []

    # we only read the first line, if there are multiple.
    # it should only be one line
    lines = load_input(2024, 9, 1, is_test)
    assert len(lines) == 1, (
        f"Expected only one line in file, got {len(lines)}"
    )
    disk_string = lines[0].strip()

    for file_id, pair in enumerate(batched(disk_string, 2)):
        f, s = 0, 0
        if len(pair) == 2:
            f, s = map(int, pair)
        else:
            f = int(pair[0])

        for _ in range(f):
            block_map += [file_id]

        for _ in range(s):
            block_map += [None]

    return block_map


def get_checksum(block_map):
    return sum(
        address * block
        for address, block in enumerate(block_map)
        if block is not None
    )
