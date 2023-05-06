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
    problem.addVariables("abcd", range(3, 100, 3))

    ab = 360
    cd = 162
    ac = 432
    bd = 135

    # problem.addConstraint(constraint.AllDifferentConstraint())
    problem.addConstraint(lambda a, b: a * b == ab, "ab")
    problem.addConstraint(lambda c, d: c * d == cd, "cd")
    problem.addConstraint(lambda a, c: a * c == ac, "ac")
    problem.addConstraint(lambda b, d: b * d == bd, "bd")
    print(f"""
   a *  b | {ab}
   c *  d | {cd}
  --   --   
  {ac}   {bd} 
    """)
    for s in problem.getSolutions():
        print(f"a = {s['a']}, b = {s['b']}, c = {s['c']}, d = {s['d']}")


if __name__ == "__main__":
    main()
