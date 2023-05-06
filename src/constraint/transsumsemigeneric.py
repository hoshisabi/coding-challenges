#!/usr/bin/python
#
#  a +  b | 57
#  c +  d | 44
# --   --
# 52   49
import constraint
from constraint import *


def main():
    problem = Problem()
    problem.addVariables("abcd", range(1, 1000))

    ab = 57
    cd = 44
    ac = 52
    bd = 49

    # problem.addConstraint(constraint.AllDifferentConstraint())
    problem.addConstraint(constraint.ExactSumConstraint(ab), "ab")
    problem.addConstraint(constraint.ExactSumConstraint(cd), "cd")
    problem.addConstraint(constraint.ExactSumConstraint(ac), "ac")
    problem.addConstraint(constraint.ExactSumConstraint(bd), "bd")
    print(f"""
   a +  b | {ab}
   c +  d | {cd}
  --   --   
  {ac}   {bd} 
    """)
    for s in problem.getSolutions():
        print(f"a = {s['a']}, b = {s['b']}, c = {s['c']}, d = {s['d']}")


if __name__ == "__main__":
    main()
