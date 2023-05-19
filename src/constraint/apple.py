from constraint import *

problem = Problem()

amounts = [20, 22, 24, 26]
baskets = ["blue", "green", "red", "white"]
names = ["berenice", "gina", "rachel", "trisha"]

criteria = baskets + names
problem.addVariables(criteria, amounts)
problem.addConstraint(AllDifferentConstraint(), names)
problem.addConstraint(AllDifferentConstraint(), baskets)

problem.addConstraint(lambda n, c: n == c, ["rachel", "white"])          # 1
problem.addConstraint(lambda n, c: n == c + 4, ["rachel", "red"])        # 2
problem.addConstraint(lambda r, w: r == 20 or w == 20, ["red", "white"]) # 3
problem.addConstraint(lambda g, b: g == 4 + b, ["gina", "berenice"])     # 4
problem.addConstraint(lambda n, c: n == c, ["berenice", "blue"])         # 5


sols = problem.getSolutions()

for sol in sols:
    for amount in amounts:
        print(f"{amount}:")
        for fact in sol:
            if sol[fact] == amount:
                print(f"  {fact}")


