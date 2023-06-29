import constraint

# Create the variables
villagers = ["hubert", "samson", "daisy", "jocelin"]
statements = ["I am the only imposter", "I am not an imposter"]

# Create the constraints
constraints = []

# The imposters will always lie, and the villagers will always tell the truth.
for i in range(len(villagers)):
    constraints.append(constraint.AllDifferentConstraint())
    constraints.append(constraint.InSetConstraint(villagers[i], statements[i]))

# The imposters will both make the same statement.
for i in range(len(villagers) - 1):
    constraints.append(constraint.EqualConstraint(statements[i], statements[i + 1]))

# The villagers will make two different statements.
for i in range(len(villagers) - 1):
    constraints.append(constraint.NotEqualConstraint(statements[i], statements[i + 1]))

# Add additional constraints to take into account the fact that the imposters and villagers can make statements about the facts.
constraints.append(constraint.BetweenConstraint(villagers, "drink", 0, 2))
constraints.append(constraint.BetweenConstraint(villagers, "drink", 2, 4))

# Solve the puzzle
solver = constraint.Solver()
solver.addConstraints(constraints)
solution = solver.solve()

# Print the solution
if solution:
    print("The imposters are:")
    for i in range(len(villagers)):
        if solution[i] == False:
            print(villagers[i])
else:
    print("No solution found")
