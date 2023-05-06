#!/usr/bin/python
#
# Korred puzzle, 9 rocks in squares, need rearranged to satisfy the rows/columns numbers
#
#   3 1 2 3
# 3 O . O O
# 2 O . . O
# 3 O . O O
# 1 . O . .


import constraint

xvals = [3, 1, 2, 3]
yvals = [3, 2, 3, 1]
rocks = 9


def print_board(d):
    s = "  " + " ".join([str(v) for v in xvals]) + "\n"
    for x in range(4):
        s += str(yvals[x]) + " "
        for y in range(4):
            s += "O " if d[(x, y)] == 1 else ". "
        s += "\n"
    print(s)


def main():
    problem = constraint.Problem()
    coords = [(x, y) for x in range(4) for y in range(4)]
    problem.addVariables(coords, range(2))
    problem.addConstraint(constraint.ExactSumConstraint(rocks))

    for y in range(4):
        problem.addConstraint(constraint.ExactSumConstraint(xvals[y]), [(x, y) for x in range(4)])
    for x in range(4):
        problem.addConstraint(constraint.ExactSumConstraint(yvals[x]), [(x, y) for y in range(4)])

    sols = problem.getSolutions()
    for s in sols:
        print_board(s)

    print(f"Exactly {len(sols)} solutions")


if __name__ == "__main__":
    main()
