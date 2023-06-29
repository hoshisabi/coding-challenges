from constraint import Problem

def solve_stable_marriage(men_preferences, women_preferences):
    problem = Problem()

    men = sorted(men_preferences.keys())
    women = sorted(women_preferences.keys())

    # Define variables representing the matches
    matches = [(man, woman) for man in men for woman in women]
    for match in matches:
        problem.addVariable(match, [0, 1])

    # Add the constraints
    # Each man is matched to exactly one woman
    for man in men:
        problem.addConstraint(lambda *matches: sum(matches) == 1, [match for match in matches if match[0] == man])

    # Each woman is matched to exactly one man
    for woman in women:
        problem.addConstraint(lambda *matches: sum(matches) == 1, [match for match in matches if match[1] == woman])

    # Add the preference constraints
    for man, preferences in men_preferences.items():
        for index, woman in enumerate(preferences):
            problem.addConstraint(lambda match, man=man, woman=woman, index=index: match[(man, woman)] == 1,
                                  [match for match in matches if match[0] == man])

    for woman, preferences in women_preferences.items():
        for index, man in enumerate(preferences):
            problem.addConstraint(lambda match, man=man, woman=woman, index=index: match[(man, woman)] == 1,
                                  [match for match in matches if match[1] == woman])

    # Solve the problem
    solutions = problem.getSolutions()

    # Get the optimal solution
    best_solution = max(solutions, key=lambda sol: sum(sum(match.values()) for match in sol.values()))

    return best_solution

# Example preferences
men_preferences = {
    'John': ['Alice', 'Catherine', 'Elizabeth'],
    'Tom': ['Catherine', 'Alice', 'Elizabeth'],
    'Mike': ['Alice', 'Elizabeth', 'Catherine']
}

women_preferences = {
    'Alice': ['Tom', 'Mike', 'John'],
    'Catherine': ['Mike', 'Tom', 'John'],
    'Elizabeth': ['John', 'Mike', 'Tom']
}

# Solve the Stable Marriage Problem
solution = solve_stable_marriage(men_preferences, women_preferences)

# Print the solution
for man, woman in solution.items():
    print(f"{man} is matched with {woman}")
