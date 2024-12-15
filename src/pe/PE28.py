
# for an x by x square
# top right corner = x^2 (for 5, 25)
# top left corner is (x^2) - (x - 1) --> (for 5, 21)
# bottom left corner is (x^2) - 2(x - 1) --> (for 5, 17)
# bottom right corner is (x^2) - 3(x - 1) --> (for 5, 13)
# total for a layer: x^2 + (x^2) - (x - 1) + (x^2) - 2(x - 1) + (x^2) - 3(x - 1)
# simplify: 4x^2 - (x - 1) - 2(x - 1) - 3(x - 1)
# simplify: 4x^2 - 6(x - 1)
# inner point is just 1
# next size must be 3
# every size beyond that is 2 larger
# 1 + fn(3) + fn(5) ... fn(n) + fn(n+2) ...

def diagonal_sum(n):
    return 1 + sum(4 * i * i - 6 * (i - 1) for i in range(3, n + 1, 2))


# Example for a 5x5 spiral
print(diagonal_sum(5))  # Output should be 101
print(diagonal_sum(7))  # Output should be ?

# For a larger spiral, say 1001x1001
print(diagonal_sum(1001))
