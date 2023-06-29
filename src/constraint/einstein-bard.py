from constraint import *

# Create variables for the houses, nationalities, pets, beverages, and cigars.
houses = ["red", "white", "yellow", "green", "blue"]
nationalities = ["Brit", "Swede", "Dane", "Norwegian", "German"]
pets = ["dogs", "birds", "horses", "fish"]
beverages = ["tea", "coffee", "milk", "water", "beer"]
cigars = ["Pall Malls", "Blends", "Dunhill", "BlueMaster", "Princes"]

# Create a problem object.
problem = Problem()

# Add variables to the problem.
for house in houses:
    problem.addVariable(house, nationalities)

# Add constraints to the problem.
for house in houses:
    problem.addConstraint(AllDifferentConstraint())

# Add clues to the problem.
problem.addConstraint(house == "red", nationalities == "Brit")
problem.addConstraint(house == "white", nationalities == "Swede")
problem.addConstraint(house == "yellow", nationalities == "Dane")
problem.addConstraint(house == "green", nationalities == "Norwegian")
problem.addConstraint(house == "blue", nationalities == "German")

problem.addConstraint(house == "red", pets == "dogs")
problem.addConstraint(house == "white", pets == "birds")
problem.addConstraint(house == "yellow", pets == "horses")
problem.addConstraint(house == "green", pets == "fish")
problem.addConstraint(house == "blue", pets == "none")

problem.addConstraint(house == "red", beverages == "tea")
problem.addConstraint(house == "white", beverages == "coffee")
problem.addConstraint(house == "yellow", beverages == "milk")
problem.addConstraint(house == "green", beverages == "water")
problem.addConstraint(house == "blue", beverages == "beer")

problem.addConstraint(house == "red", cigars == "Pall Malls")
problem.addConstraint(house == "white", cigars == "Blends")
problem.addConstraint(house == "yellow", cigars == "Dunhill")
problem.addConstraint(house == "green", cigars == "BlueMaster")
problem.addConstraint(house == "blue", cigars == "Princes")

# Solve the problem.
solution = problem.getSolution()

# Print the solution.
if solution is not None:
    print("The German owns the fish.")
else:
    print("There is no solution.")