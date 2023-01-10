import heapq

elves = []
elf = 0
# input_file = "aoc2022-01-testinput.txt"
input_file = "aoc2022-01-input.txt"

with open(input_file) as f:
    for t in f:
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

