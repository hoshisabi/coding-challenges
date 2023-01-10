#!/usr/bin/python
#
# Assign equal values to equal letters, and different values to
# different letters, in a way that satisfies the following sum:
#
#    BASE
#  + BALL
#  ------
#   GAMES
#
from constraint import *


def main():
    problem = Problem()
    problem.addVariables("baselgm", range(10))
    problem.addConstraint(lambda e, l, s: (e + l) % 10 == s, "els")
    problem.addConstraint(lambda e, l, s: (s * 10 + e + l * 10 + l) % 100 == e * 10 + s, "els")
    problem.addConstraint(lambda e, l, s, a, m:
                          (a * 100 + s * 10 + e + a * 100 + l * 10 + l) % 1000 == m * 100 + e * 10 + s,
                          "elsam")
    problem.addConstraint(lambda b, a, s, e, l, g, m:
                          1000 * b + 100 * a + 10 * s + e + 1000 * b + 100 * a + 10 * l + l ==
                          10000 * g + 1000 * a + 100 * m + 10 * e + s, "baselgm")
    problem.addConstraint(NotInSetConstraint({0}), "bg")
    problem.addConstraint(AllDifferentConstraint())
    print("BASE+BALL=GAMES")
    for s in problem.getSolutions():
        print(f"{s['b']}{s['a']}{s['s']}{s['e']}+"
              f"{s['b']}{s['a']}{s['l']}{s['l']}="
              f"{s['g']}{s['a']}{s['m']}{s['e']}{s['s']}")


if __name__ == "__main__":
    main()
