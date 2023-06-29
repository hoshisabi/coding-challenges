from constraint import *
from itertools import combinations

problem = Problem()

men = ["a", "b", "c", "d"]
women = ["1", "2", "3", "4"]

preferences = {
    "a": ["1", "2", "3", "4"],
    "b": ["2", "1", "3", "4"],
    "c": ["3", "2", "1", "4"],
    "d": ["4", "2", "3", "1"],
    "1": ["a", "b", "c", "d"],
    "2": ["b", "a", "c", "d"],
    "3": ["c", "b", "a", "d"],
    "4": ["d", "b", "c", "a"],
}

problem.addVariables(men + women, men + women)

# Each man must be matched with exactly one woman.
for man in men:
    problem.addConstraint(AllDifferentConstraint())

# Each woman must be matched with exactly one man.
for woman in women:
    problem.addConstraint(AllDifferentConstraint())

# No two men can be matched with the same woman.
for man1, man2 in combinations(men, 2):
    for woman in preferences[man1]:
        if woman in preferences[man2]:
            #problem.addConstraint(NotInSetConstraint({man2}, [woman]))
            problem.addConstraint(NotInSetConstraint({man2}, woman))

# No two women can be matched with the same man.
for woman1, woman2 in combinations(women, 2):
    for man in preferences[woman1]:
        if man in preferences[woman2]:
            #problem.addConstraint(NotInSetConstraint({woman2}, [man]))
            problem.addConstraint(NotInSetConstraint({woman2}, man))

sols = problem.getSolutions()

for sol in sols:
    print(sol)
