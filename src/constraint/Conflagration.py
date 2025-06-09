from constraint import Problem, AllDifferentConstraint, InSetConstraint

materials = ["Brass", "Clay", "Copper", "Glass"]
liquids = ["Black", "Green", "Orange", "Purple"]
positions = range(1, len(materials) + 1)

problem = Problem()

# Each position gets a material and a liquid
problem.addVariables(materials, positions)  # Assign positions to materials
problem.addVariables(liquids, positions)    # Assign positions to liquids

# Enforce uniqueness (each cup has a distinct material & liquid)
problem.addConstraint(AllDifferentConstraint(), materials)
problem.addConstraint(AllDifferentConstraint(), liquids)

# Apply constraints
# THE CLAY CUP POURED EITHER ORANGE OR PURPLE.
problem.addConstraint(
    lambda clay, orange, purple: clay == orange or clay == purple,
    ["Clay", "Orange", "Purple"]
)
# THE GLASS CUP WAS USED SECOND.
problem.addConstraint(InSetConstraint([2]), ["Glass"])
# THE BLACK LIQUID MUST BE POURED JUST BEFORE THE COPPER CUP IS USED.
problem.addConstraint(
    lambda black, copper: copper == black + 1,
    ["Black", "Copper"]
)
# THE ORANGE LIQUID MUST BE POURED SECOND.
problem.addConstraint(InSetConstraint([2]), ["Orange"])

# Solve and display formatted results
solutions = problem.getSolutions()

for sol in solutions:
    inverted_map = {}
    # Reverse-map materials and liquids to their assigned positions
    for key, value in sol.items():
        if value not in inverted_map:
            inverted_map[value] = {}
        inverted_map[value][key] = value

    print("--------")
    for position in sorted(inverted_map.keys()):
        material = [k for k in inverted_map[position] if k in materials][0]
        liquid = [k for k in inverted_map[position] if k in liquids][0]
        print(f"{position}: {material}, {liquid}")