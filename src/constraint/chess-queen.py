#!/usr/bin/python
#
# Queens Puzzle
# In chess, the queen can move any number of squares in any one direction, vertically, horizontally, or diagonally.
# The Eight Queen Puzzle requires that you place 8 queens on a standard chess board where none of the other queens can
# capture the others.

import constraint

queens = 5

xsize = 8
ysize = 8

def print_board(d):
    s = ""
    for x in range(xsize):
        for y in range(ysize):
            s += "Q " if d[(x, y)] == 1 else ". "
        s += "\n"
    print(s)


def main():
    problem = constraint.Problem()
    coords = [(x,y) for x in range(xsize) for y in range(ysize)]
    problem.addVariables(coords, range(2))
    problem.addConstraint(constraint.ExactSumConstraint(queens))

    for x in range(xsize):
        problem.addConstraint(constraint.MaxSumConstraint(1), [(x,y) for y in range(ysize)])
    for y in range(ysize):
        problem.addConstraint(constraint.MaxSumConstraint(1), [(x,y) for x in range(xsize)])

    sols = problem.getSolutions()
    for s in sols:
        print_board(s)



if __name__ == "__main__":
    main()


