from constraint import Problem, AllDifferentConstraint, InSetConstraint, SomeInSetConstraint

# Expected solution:
# 1: Glass, Orange, Translucent
# 2: Brass, Black, Acidic
# 3: Copper, Purple, Alkaline
# 4: Clay, Green, Viscous    

materials = ["Brass", "Clay", "Copper", "Glass"]
liquids = ["Black", "Green", "Orange", "Purple"]
properties = ["Acidic", "Alkaline", "Translucent", "Viscous"]
positions = range(1, len(materials) + 1)

problem = Problem()

# Each position gets a material, a liquid, and a property
problem.addVariables(materials, positions)    # Assign positions to materials
problem.addVariables(liquids, positions)      # Assign positions to liquids
problem.addVariables(properties, positions)   # Assign positions to properties

# Enforce uniqueness (each cup has a distinct material, liquid & property)
problem.addConstraint(AllDifferentConstraint(), materials)
problem.addConstraint(AllDifferentConstraint(), liquids)
problem.addConstraint(AllDifferentConstraint(), properties)

# Apply constraints
# 1. Allow the light to shine through the first cup before any other cups are filled.
problem.addConstraint(InSetConstraint([1]), ["Glass"])  
# 2. Avoid breathing in the fumes as you pour the liquid into the second cup.
problem.addConstraint(SomeInSetConstraint([2]), ["Acidic", "Alkaline"])  
# 3. The next liquid will form a blueish patina in its cup before you are finished.
problem.addConstraint(InSetConstraint([3]), ["Copper", "Alkaline"])  
# 4. The green liquid must be poured last to avoid it seeping through the cup.
problem.addConstraint(InSetConstraint([4]), ["Clay", "Green"])  # Green must be in position 4

# ----
# Fact: The purple liquid has a pungent odor.
problem.addConstraint(lambda purple, alkaline: purple == alkaline, ["Purple", "Alkaline"])
# Fact: The black liquid has a sharp, sour smell.
problem.addConstraint(lambda black, acidic: black == acidic, ["Black", "Acidic"])
# Fact: The orange liquid is translucent, thin, and has no noticeable odor.
problem.addConstraint(lambda orange, translucent: orange == translucent, ["Orange", "Translucent"])
# Fact: The green liquid is thick and smells like honey.
problem.addConstraint(lambda green, viscous: green == viscous, ["Green", "Viscous"])

# Solve and display formatted results
solutions = problem.getSolutions()

print(f"Found {len(solutions)} solutions:")
for sol in solutions:
    inverted_map = {}
    # Reverse-map materials, liquids, and properties to their assigned positions
    for key, value in sol.items():
        if value not in inverted_map:
            inverted_map[value] = {}
        inverted_map[value][key] = value

    print("--------")
    for position in sorted(inverted_map.keys()):
        material = [k for k in inverted_map[position] if k in materials][0]
        liquid = [k for k in inverted_map[position] if k in liquids][0]
        property = [k for k in inverted_map[position] if k in properties][0]
        print(f"{position}: {material}, {liquid}, {property}")

print(f"Found {len(solutions)} solutions.")
