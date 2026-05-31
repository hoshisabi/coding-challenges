#!/usr/bin/python
#
# log-mc-002-shelf-puzzle
#
# A 3x3 shelf grid (positions 0-8):
#   TL(0) | TM(1) | TR(2)   <- top row
#   ML(3) | MM(4) | MR(5)   <- middle row
#   BL(6) | BM(7) | BR(8)   <- bottom row
#
# Items: Ale, Beans, Cat Food, Dried Fish, Grog,
#        Oranges, Salt Pork, Spices, Vegetables
#
# Constraints:
# 1. "Put the ale in a corner so it won't get knocked over."
# 2. "Veg stays on the bottom row. Barely use it."
# 3. "Beans are below the oranges. Don't ask me why."
#    → directly below: same column, one row down
# 4. "Keep the spices under the ale somewhere. It's easier to grab."
#    → same column as ale, any lower row
# 5. "Citrus goes beside the ale. It cuts the stink."
#    → same row, adjacent column
# 6. "Smokepowder's food goes under the fish. Cat won't eat it otherwise."
#    → directly below: same column, one row down
# 7. "Keep the salt pork away from the cat food. He hates the stuff."
#    → not adjacent (including diagonals, i.e. Chebyshev distance > 1)
# 8. "Whatever's left, just stick it in the last spot!" (Grog; no constraints)

# As written, three solutions?
# Solution 1:
# |        | Left       | Middle     | Right      |
# |--------|------------|------------|------------|
# | Top    | Grog       | Oranges    | Ale        |
# | Middle | Dried Fish | Beans      | Salt Pork  |
# | Bottom | Cat Food   | Veg        | Spices     |

# Solution 2:
# |        | Left       | Middle     | Right      |
# |--------|------------|------------|------------|
# | Top    | Dried Fish | Oranges    | Ale        |
# | Middle | Cat Food   | Beans      | Spices     |
# | Bottom | Veg        | Grog       | Salt Pork  |

# Solution 3:
# |        | Left       | Middle     | Right      |
# |--------|------------|------------|------------|
# | Top    | Dried Fish | Oranges    | Ale        |
# | Middle | Cat Food   | Beans      | Spices     |
# | Bottom | Grog       | Veg        | Salt Pork  |

# SUGGESTION TO PUZZLE AUTHOR:
# Solutions 2 and 3 (and their reflections) differ only in whether Grog or Veg
# occupies the corner vs. the middle of the bottom row. The official solution
# has Veg in the middle and Grog in the corner, but no existing clue distinguishes
# this. A hint such as "Grog goes in the corner, out of the way" or
# "Veg stays in the middle of the bottom row" would make the solution unique.

from constraint import AllDifferentConstraint, Problem

ROW_LABELS = ["Top", "Middle", "Bottom"]


def row(pos):
    return pos // 3


def col(pos):
    return pos % 3


def chebyshev_adjacent(p, q):
    return max(abs(row(p) - row(q)), abs(col(p) - col(q))) <= 1


def manhattan(p, q):
    return abs(row(p) - row(q)) + abs(col(p) - col(q))


# Horizontal mirror: col 0 <-> col 2, col 1 stays
_MIRROR = {0: 2, 1: 1, 2: 0, 3: 5, 4: 4, 5: 3, 6: 8, 7: 7, 8: 6}


def canonical(sol):
    """Return a key that is the same for a solution and its horizontal reflection."""
    orig = tuple(sorted(sol.items()))
    mirrored = tuple(sorted((item, _MIRROR[pos]) for item, pos in sol.items()))
    return min(orig, mirrored)


def deduplicate_reflections(solutions):
    seen, unique = set(), []
    for sol in solutions:
        key = canonical(sol)
        if key not in seen:
            seen.add(key)
            unique.append(sol)
    return unique


def main():
    problem = Problem()

    items = [
        "ale",
        "beans",
        "cat_food",
        "dried_fish",
        "grog",
        "oranges",
        "salt_pork",
        "spices",
        "veg",
    ]
    problem.addVariables(items, range(9))
    problem.addConstraint(AllDifferentConstraint(), items)

    # 1. Ale in a corner: TL(0), TR(2), BL(6), BR(8)
    problem.addConstraint(lambda ale: ale in (0, 2, 6, 8), ["ale"])

    # 2. Veg on bottom row
    problem.addConstraint(lambda veg: row(veg) == 2, ["veg"])

    # 3. Beans directly below oranges (same column, one row down)
    problem.addConstraint(
        lambda beans, oranges: (
            col(beans) == col(oranges) and row(beans) == row(oranges) + 1
        ),
        ["beans", "oranges"],
    )

    # 4. Spices in same column as ale, any lower row
    problem.addConstraint(
        lambda spices, ale: col(spices) == col(ale) and row(spices) > row(ale),
        ["spices", "ale"],
    )

    # 5. Oranges beside ale: same row, adjacent column
    problem.addConstraint(
        lambda oranges, ale: (
            row(oranges) == row(ale) and abs(col(oranges) - col(ale)) == 1
        ),
        ["oranges", "ale"],
    )

    # 6. Cat food directly below dried fish (same column, one row down)
    problem.addConstraint(
        lambda cat_food, dried_fish: (
            col(cat_food) == col(dried_fish) and row(cat_food) == row(dried_fish) + 1
        ),
        ["cat_food", "dried_fish"],
    )

    # 7. Salt pork not adjacent to cat food (including diagonals)
    problem.addConstraint(
        lambda salt_pork, cat_food: not chebyshev_adjacent(salt_pork, cat_food),
        ["salt_pork", "cat_food"],
    )

    # 8. Grog: no constraints ("whatever's left")

    solutions = problem.getSolutions()

    # "Pork is as far from the cat food as possible" — keep only max-distance solutions
    def sp_cf_dist(sol):
        return manhattan(sol["salt_pork"], sol["cat_food"])

    max_dist = max(sp_cf_dist(s) for s in solutions)
    solutions = [s for s in solutions if sp_cf_dist(s) == max_dist]

    solutions = deduplicate_reflections(solutions)
    print(
        f"Found {len(solutions)} solution(s) with max Salt Pork <-> Cat Food distance = {max_dist} (reflections merged)\n"
    )
    for i, sol in enumerate(solutions, 1):
        print(f"Solution {i}:")
        print_grid(sol)

    print_tsv(solutions)


LABEL = {
    "ale": "Ale",
    "beans": "Beans",
    "cat_food": "Cat Food",
    "dried_fish": "Dried Fish",
    "grog": "Grog",
    "oranges": "Oranges",
    "salt_pork": "Salt Pork",
    "spices": "Spices",
    "veg": "Veg",
}


def print_tsv(solutions):
    print("\t".join(["solution", "row", "left", "middle", "right"]))
    for i, sol in enumerate(solutions, 1):
        grid = {v: k for k, v in sol.items()}
        for r, label in enumerate(ROW_LABELS):
            cells = [LABEL[grid[r * 3 + c]] for c in range(3)]
            print("\t".join([str(i), label] + cells))


def print_grid(solution):
    grid = {v: k for k, v in solution.items()}
    rows = [[LABEL[grid[r * 3 + c]] for c in range(3)] for r in range(3)]

    # Plain grid
    for r, cells in enumerate(rows):
        print(f"  {ROW_LABELS[r]:<8} {cells[0]:<12} | {cells[1]:<12} | {cells[2]:<12}")

    # Markdown table
    print()
    print("|        | Left       | Middle     | Right      |")
    print("|--------|------------|------------|------------|")
    for r, cells in enumerate(rows):
        print(
            f"| {ROW_LABELS[r]:<6} | {cells[0]:<10} | {cells[1]:<10} | {cells[2]:<10} |"
        )
    print()


if __name__ == "__main__":
    main()
