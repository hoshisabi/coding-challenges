#!/usr/bin/python
#
#   a +   b | 163
#   c +   d | 140
# ---   ---
# 153   150
import constraint
from constraint import *


def main():
    problem = Problem()
    problem.addVariables("abcd", range(1, 1000))
    problem.addConstraint(constraint.AllDifferentConstraint())
    problem.addConstraint(constraint.ExactSumConstraint(163), "ab")
    problem.addConstraint(constraint.ExactSumConstraint(140), "cd")
    problem.addConstraint(constraint.ExactSumConstraint(153), "ac")
    problem.addConstraint(constraint.ExactSumConstraint(150), "bd")
    print("""
   a +   b | 163
   c +   d | 140
 ---   ---   
 153   150 
    """)
    for s in problem.getSolutions():
        print(f"a = {s['a']}, b = {s['b']}, c = {s['c']}, d = {s['d']}")


if __name__ == "__main__":
    main()
