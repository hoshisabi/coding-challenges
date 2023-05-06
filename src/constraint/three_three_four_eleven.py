#!/usr/bin/python
#
# Assign equal values to equal letters, and different values to
# different letters, in a way that satisfies the following sum:
#
#    THREE
#  + THREE
#  +  FOUR
#   ------
#   ELEVEN
#
from constraint import *


def main():
    problem = Problem()
    problem.addVariables("threfoulvn", range(10))
    problem.addConstraint(lambda e, r, n:
                          (e * 2 + r) % 10 == n,
                          "ern")
    problem.addConstraint(lambda e, r, n, u:
                          (e * 20 + e * 2 + u * 10 + r) % 100 ==
                          e * 10 + n,
                          "ernu")
    problem.addConstraint(lambda e, r, n, u, o, v:
                          (r * 200 + e * 20 + e * 2 + o * 100 + u * 10 + r) % 1000 ==
                          v * 100 + e * 10 + n,
                          "ernuov")
    problem.addConstraint(lambda e, r, n, u, o, v, h, f:
                          (h * 2000 + r * 200 + e * 20 + e * 2 + f * 1000 + o * 100 + u * 10 + r) % 10000 ==
                          e * 1000 + v * 100 + e * 10 + n,
                          "ernuovhf")
    problem.addConstraint(lambda e, r, n, u, o, v, h, f, t, l:
                          (t * 20000 + h * 2000 + r * 200 + e * 20 + e * 2 + f * 1000 + o * 100 + u * 10 + r) % 100000 ==
                          l * 10000 + e * 1000 + v * 100 + e * 10 + n,
                          "ernuovhftl")
    problem.addConstraint(lambda e, r, n, u, o, v, h, f, t, l:
                          t * 20000 + h * 2000 + r * 200 + e * 20 + e * 2 + f * 1000 + o * 100 + u * 10 + r ==
                          e * 100000 + l * 10000 + e * 1000 + v * 100 + e * 10 + n,
                          "ernuovhftl")
    problem.addConstraint(NotInSetConstraint({0}), "tfe")
    problem.addConstraint(AllDifferentConstraint())
    print("THREE+THREE+FOUR=ELEVEN")
    for s in problem.getSolutions():
        print(f"{s['t']}{s['h']}{s['r']}{s['e']}{s['e']}+"
              f"{s['t']}{s['h']}{s['r']}{s['e']}{s['e']}+"
              f"{s['f']}{s['o']}{s['u']}{s['r']}="
              f"{s['e']}{s['l']}{s['e']}{s['v']}{s['e']}{s['n']}")


if __name__ == "__main__":
    main()
