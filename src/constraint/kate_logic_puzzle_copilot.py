from constraint import Problem

# Create the problem
problem = Problem()

# Define variables and domains
names = ["Winifred", "Eleanor", "Isabelle", "George", "Harold", "Amy", "Zoe"]
horn_colors = ["red", "yellow", "blue", "green", "purple", "orange", "gold"]

# Add variables: Pair each name with a horn color
problem.addVariables(names, horn_colors)

# Define constraints
# 1. Unicorns don't pair with those who share the first letter of their name
problem.addConstraint(lambda name, color: name[0].lower() != color[0].lower(), names)

# 2. Unicorns with 8-letter names must have primary colors
primary_colors = {"red", "yellow", "blue"}
problem.addConstraint(lambda name, color: (len(name) == 8 and color in primary_colors) or len(name) != 8, names)

# 3. Primary colors pair with complementary secondary colors
complementary = {"red": "green", "yellow": "purple", "blue": "orange"}
problem.addConstraint(lambda color1, color2: complementary.get(color1.lower()) == color2.lower(),
                      horn_colors)

# 4. Names starting with 'W' must have warm tones
warm_colors = {"red", "orange"}
problem.addConstraint(lambda name, color: (name.startswith('W') and color in warm_colors) or not name.startswith('W'), names)

# 5. Double-vowel names pair
import re
vowels = "aeiou"
double_vowel_names = [name for name in names if re.search(f"(?i){vowels}.*{vowels}", name)]
problem.addConstraint(lambda name, color: (name in double_vowel_names) == (color in double_vowel_names), names)

# 6. Winifred's partner has the same number of vowels in their name
def count_vowels(name):
    return len(re.findall(f"(?i){vowels}", name))

problem.addConstraint(lambda name, color: name != "Winifred" or count_vowels(name) == count_vowels(color), names)

# Solve the problem
solutions = problem.getSolutions()

# Print the solutions
if solutions:
    for solution in solutions:
        print(solution)
else:
    print("No solutions found.")