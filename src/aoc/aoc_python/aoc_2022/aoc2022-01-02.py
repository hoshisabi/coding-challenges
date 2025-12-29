import heapq

from aoc_shared.aoc_tools import load_input

elves = []
elf = 0
# input_file = load_input(2022, 1, 2, True)
lines = load_input(2022, 1, 2, False)

for t in lines:
    line = t.strip()
    calories = int(line) if len(line) > 0 else 0
    if calories > 0:
        print(f"adding {calories} calories to elf {elf}")
        elf += calories
    else:
        print(f"adding {elf} elf to list")
        if elf > 0:
            elves += [elf]
        elf = 0

if elf > 0:
    elves += [elf]

print(elves)
print(sum(heapq.nlargest(3, elves)))

