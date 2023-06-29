from constraint import *

problem = Problem()

men = ["alvin", "bob", "charles"]
women = ["alice", "barb", "connie"]

men_prefs = {
    "alvin": ["alice", "barb", "connie"],
    "bob": ["barb", "alice", "connie"],
    "charles": ["connie", "barb", "alice"],
}

women_prefs = {
    "alice": ["alvin", "bob", "charles"],
    "barb": ["alvin", "bob", "charles"],
    "connie": ["alvin", "bob", "charles"],
}


def compare_spouse_for_man(man, woman1, woman2):
    return men_prefs[man].index(woman1) < men_prefs[man].index(woman2)


def compare_spouse_for_woman(woman, man1, man2):
    return women_prefs[woman].index(man1) < women_prefs[woman].index(man2)


problem.addConstraint(AllDifferentConstraint(), women)
problem.addConstraint(AllDifferentConstraint(), men)
problem.addConstraint()

for man in men:
    problem.addVariable(man, women)

for woman in women:
    problem.addVariable(woman, men)

sols = problem.getSolutions()
for sol in sols:
    print(sol)

print(f"Number of sols: {len(sols)}")
