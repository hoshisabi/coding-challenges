from aoc_shared.aoc_tools import load_input

# input_file = load_input(2022, 2, 1, True)
lines = load_input(2022, 2, 1, False)


# A = rock          X = rock
# B = paper         Y = paper
# C = scissors      Z = scissors
scores = {
    "A X": [4, "rock vs ROCK"],
    "A Y": [8, "rock vs PAPER"],
    "A Z": [3, "rock vs SCISSORS"],
    "B X": [1, "paper vs ROCK"],
    "B Y": [5, "paper vs PAPER"],
    "B Z": [9, "paper vs SCISSORS"],
    "C X": [7, "scissors vs ROCK"],
    "C Y": [2, "scissors vs PAPER"],
    "C Z": [6, "scissors vs SCISSORS"],
}

total = 0
for t in lines:
    line = t.strip()
    round = scores[line]
    print(round)
    total += round[0]

print(f"Total score {total}")
