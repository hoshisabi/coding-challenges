# 1. Unicorns don't pair with those who share the 1st letter of their name
# 2. Unicorns with 8 letter names have horns of primary colors.
# 3. Primary colors pair with complementary secondary colors.
# 4. Names starting with W have warm tones.
# 5. Double-vowel names pair.
# 6. Winifred's pair has the same number of vowels in their name as they do.
# 7. Gold belongs to the shortest name.
# Given 1: Your partner has you as their partner
# Given 2: You cannot partner with yourself.
# Given 3: Primary colors: "red", "yellow", "blue"
# Given 4: Complementary secondary colors: red -> green, yellow -> purple, blue -> orange
# Given 5: Warm tones: red and orange
# Given 6: Vowels: aeiou

import constraint
import re

problem = constraint.Problem()
names = ["Alistair", "Archibald", "Bonnie", "Edwin", "Florence", "Oswald", "Winifred", "Winston"]
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Silver", "Gold"]
complementary = {"red": "green", "yellow": "purple", "blue": "orange"}
warm = {"red", "orange"}
primary = {"red", "yellow", "blue"}
vowels = "[aeiou]"

eight_names = list(filter(lambda n: len(n) == 8, names))
double_vowels = list(filter(lambda n: re.search("(?i)" + vowels + "{2}", n), names))


def count_vowels(n):
    return len(re.findall("(?i)" + vowels, n))


problem.addVariables(["name",  "partner"], names)
problem.addVariable("color", colors)


problem.addConstraint(lambda n, p: n != p, ["name", "partner"])
problem.addConstraint(lambda n, p: n[0] != p[0], ["name", "partner"])
problem.addConstraint(lambda n, p: (n in double_vowels and p in double_vowels) or
                                   (n not in double_vowels and p not in double_vowels),
                      ["name", "partner"])
problem.addConstraint(lambda n, c: (n not in eight_names) or
                                   (n in eight_names and c in primary),
                      ["name", "color"])
problem.addConstraint(lambda n, c: (n[0] == "w" and c in warm) or
                                   (n[0] != "w"),
                      ["name", "color"])
problem.addConstraint(lambda n, p: n != "Winifred" or
                                   (n == "Winifred" and count_vowels(p) == count_vowels(n)),
                      ["name", "partner"])


print(problem.getSolutions())
