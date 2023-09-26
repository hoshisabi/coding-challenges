# import re
import json

letter_score = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1, 't': 1, 'u': 1,
                'd': 2, 'g': 2,
                'b': 3, 'c': 3, 'm': 3, 'p': 3,
                'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
                'k': 5,
                'j': 8, 'x': 8,
                'q': 10, 'z': 10}


def scrabble_score(word_to_score):
    return sum(letter_score[_] for _ in word_to_score)


def filter_by_color(word_to_filter) -> bool:
    if len(word_to_filter) != 5:
        return False

    yl = set("".join(yellow.values()))
    for i in range(5):
        if black and word_to_filter[i] in black:
            return False
        if yellow[i] and word_to_filter[i] in yellow[i]:
            return False
        if green[i] and word_to_filter[i] != green[i]:
            return False

    return all(_ in word_to_filter for _ in yl)


# Empty start:
# black = ''
# yellow = {0: '', 1: '', 2: '', 3: '', 4: ''}
# green = {0: '', 1: '', 2: '', 3: '', 4: ''}

black = ''
yellow = {0: '', 1: '', 2: '', 3: '', 4: ''}
green = {0: '', 1: '', 2: '', 3: '', 4: ''}

with open('../conf/5letter.json') as f:
    valid_words = json.load(f)

filtered_words = list(filter(filter_by_color, valid_words))
print(f"Size: {len(filtered_words)}")
for word in filtered_words:
    score = scrabble_score(word)
    print(f"{word}: {score}")
