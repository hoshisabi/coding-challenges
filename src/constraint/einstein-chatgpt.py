from constraint import Problem

def solve_einstein_puzzle():
    problem = Problem()

    # Define variables representing the different attributes
    attributes = ['nationality', 'house_color', 'pet', 'drink', 'cigarette']

    # Define domains for each attribute
    domains = {
        'nationality': ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese'],
        'house_color': ['Red', 'Green', 'Ivory', 'Yellow', 'Blue'],
        'pet': ['Dog', 'Snails', 'Fox', 'Horse', 'Zebra'],
        'drink': ['Coffee', 'Tea', 'Milk', 'Orange Juice', 'Water'],
        'cigarette': ['Old Gold', 'Kools', 'Chesterfields', 'Lucky Strike', 'Parliaments']
    }

    # Add variables to the problem
    for attribute in attributes:
        problem.addVariable(attribute, domains[attribute])

    # Add constraints based on the given clues
    problem.addConstraint(lambda n1, c1: n1 == c1, ['nationality', 'house_color'])
    problem.addConstraint(lambda n2, p1: n2 == p1, ['nationality', 'pet'])
    problem.addConstraint(lambda c2, c3: c2 == c3, ['house_color', 'drink'])
    problem.addConstraint(lambda n3, c4: n3 == c4, ['nationality', 'drink'])
    problem.addConstraint(lambda c5: c5 == 'Green', ['house_color'])
    problem.addConstraint(lambda h1: h1 == 'Ivory' + 1, ['house_color'])
    problem.addConstraint(lambda n4, c6: n4 == c6, ['nationality', 'pet'])
    problem.addConstraint(lambda c7, d1: c7 == d1, ['cigarette', 'house_color'])
    problem.addConstraint(lambda h2: h2 == 'Milk', ['drink'])
    problem.addConstraint(lambda n5, c8: n5 == c8, ['nationality', 'house_color'])
    problem.addConstraint(lambda c9, c10: c9 == c10, ['cigarette', 'pet'])
    problem.addConstraint(lambda c11, d2: c11 == d2, ['cigarette', 'drink'])
    problem.addConstraint(lambda n6, c12: n6 == c12, ['nationality', 'drink'])
    problem.addConstraint(lambda n7, c13: n7 == c13, ['nationality', 'cigarette'])
    problem.addConstraint(lambda h3: h3 == 'Blue' - 1, ['house_color'])

    # Solve the problem
    solution = problem.getSolution()

    return solution

# Solve Einstein's Puzzle
solution = solve_einstein_puzzle()

# Print the solution
for attribute, value in solution.items():
    print(f"{attribute}: {value}")
