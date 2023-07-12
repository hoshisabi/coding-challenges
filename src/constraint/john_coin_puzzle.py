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
# ABC
# D_E
# FGH

from constraint import *

expected_sum = 9
total_sum_max = 28

def main():
    problem = Problem()
    problem.addVariables("abcdefgh", range(1,10))
    problem.addConstraint(MaxSumConstraint(total_sum_max), "abcdefgh")

    # ABC
    # D_E
    # FGH
    problem.addConstraint(lambda x, y, z: x+y+z == expected_sum, "abc")
    problem.addConstraint(lambda x, y, z: x+y+z == expected_sum, "fgh")
    problem.addConstraint(lambda x, y, z: x+y+z == expected_sum, "adf")
    problem.addConstraint(lambda x, y, z: x+y+z == expected_sum, "ceh")


    sols = problem.getSolutions()
    min_sum = 99
    poss_sol = {}
    for sol in sols:
        sol_sum = sum(sol.values())
        if sol_sum < min_sum:
            min_sum = sol_sum
            poss_sol = sol

    print(f"Minimum sum {min_sum}")
    print(f"{poss_sol['a']}{poss_sol['b']}{poss_sol['c']}\n"
          f"{poss_sol['d']}_{poss_sol['e']}\n"
          f"{poss_sol['f']}{poss_sol['g']}{poss_sol['h']}")


if __name__ == "__main__":
    main()
