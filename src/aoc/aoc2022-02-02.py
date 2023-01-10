# input_file = "aoc2022-02-testinput.txt"
input_file = "aoc2022-02-input.txt"

# A = rock          X = lose
# B = paper         Y = draw
# C = scissors      Z = win
rock = 1
paper = 2
scissors = 3
lose = 0
draw = 3
win = 6

scores = {
    "A X": [scissors + lose, "rock vs SCISSORS [lose]"],
    "A Y": [rock + draw, "rock vs ROCK [draw]"],
    "A Z": [paper + win, "rock vs PAPER [win]"],
    "B X": [rock + lose, "paper vs ROCK [lose]"],
    "B Y": [paper + draw, "paper vs PAPER [draw]"],
    "B Z": [scissors + win, "paper vs SCISSORS [win]"],
    "C X": [paper + lose, "scissors vs PAPER [lose]"],
    "C Y": [scissors + draw, "scissors vs SCISSORS [draw]"],
    "C Z": [rock + win, "scissors vs ROCK [win]"],
}

total = 0
with open(input_file) as f:
    for t in f:
        line = t.strip()
        round = scores[line]
        print(round)
        total += round[0]

print(f"Total score {total}")
