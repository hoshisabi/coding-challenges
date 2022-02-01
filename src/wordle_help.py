# import re
import json

letter_score = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
                'd': 2, 'g': 2,
                'b': 3, 'c': 3, 'm': 3, 'p': 3,
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
                'k': 5,
                'j': 8, 'x': 8,
                'q': 10, 'z': 10}


def scrabble_score(word):
    return sum(letter_score[l] for l in word)


def filter_by_color(word) -> bool:
    if len(word) != 5:
        return False

    yl = sum(yellow.values(), [])

    for i in range(5):
        if black and word[i] in black:
            return False
        if yellow[i] and word[i] in yellow[i]:
            return False
        if green[i] and word[i] != green[i]:
            return False

    return all(l in word for l in yl)


# Empty start:
# black = ''
# yellow = {0: [], 1: [], 2: [], 3: [], 4: []}
# green = {0: '', 1: '', 2: '', 3: '', 4: ''}

black = 'shatoungmb'
yellow = {0: ['r'], 1: ['e'], 2: [], 3: ['i', 'r'], 4: []}
green = {0: '', 1: 'r', 2: 'i', 3: 'd', 4: 'e'}

with open('../conf/5letter.json') as f:
    valid_words = json.load(f)

filtered_words = list(filter(filter_by_color, valid_words.keys()))
print(f"Size: {len(filtered_words)}")
for word in filtered_words:
    score = scrabble_score(word)
    print(f"{word}: {score}")
