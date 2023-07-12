#!/usr/bin/python
#
# puzzle:
# 2 5 2
# 5 _ 5     (max sum 28)
# 2 5 2
# can be turned into
# 4 1 4
# 1 _ 1     (max sum 20)
# 4 1 4
# max sum of
# constraint:
# outer rows/columns exact sum of 9
# middle cell must be 0
# outer cells must be 1 or greater
# total of all cells must be less than 28
# win condition, minimum total of all cells
# Cells:
# OEO
# E_E
# OEO

from constraint import *

expected_sum = 9

def main():
    problem = Problem()
    problem.addVariables("oe", range(1,10))
    problem.addConstraint(lambda o, e: 2 * o + e == expected_sum, "oe")

    sols = problem.getSolutions()
    min_sum = 99
    poss_sol = {}
    for sol in sols:
        sol_sum = 4 * sol['o'] + 4 * sol['e']
        if sol_sum < min_sum:
            min_sum = sol_sum
            poss_sol = sol

    print(f"Minimum sum {min_sum}")
    print(f"{poss_sol['o']}{poss_sol['e']}{poss_sol['o']}\n"
          f"{poss_sol['e']}_{poss_sol['e']}\n"
          f"{poss_sol['o']}{poss_sol['e']}{poss_sol['o']}")


if __name__ == "__main__":
    main()
