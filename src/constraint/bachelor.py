from constraint import *

problem = Problem()

hosts = ["andy", "bill", "carl", "dave", "eric"]
foods = ["fish", "pizza", "steak", "tacos", "thai"]
days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

criteria = foods + days
problem.addVariables(criteria, hosts)
problem.addConstraint(AllDifferentConstraint(), foods)
problem.addConstraint(AllDifferentConstraint(), days)

# Eric was not Friday's host
problem.addConstraint(NotInSetConstraint({"eric"}), ["friday"])

# Carl hosted the group on Wednesday
problem.addConstraint(InSetConstraint({"carl"}), ["wednesday"])

# The fellows ate at a Thai place on Friday
problem.addConstraint(lambda f, d: f == d, ["thai", "friday"])

# Bill, who detests fish, volunteered to be the first host
problem.addConstraint(NotInSetConstraint({"bill"}), ["fish"])
problem.addConstraint(InSetConstraint({"bill"}), ["monday"])

# Dave selected a steak house for the night before one of the follows hosted everyone at a pizza parlor
problem.addConstraint(InSetConstraint({"dave"}), ["steak"])
problem.addConstraint(NotInSetConstraint({"dave"}), ["friday"])
problem.addConstraint()
sols = problem.getSolutions()
for i, sol in enumerate(sols, start=1):
    print(f"-----------{i}-----------")
    for host in hosts:
        print(f"{host}:")
        for fact in sol:
            if sol[fact] == host:
                print(f"  {fact}")


