def dot_print(array):
    """
    Pretty print a binary or boolean array.
    """
    for row in array:
        print("".join(" #"[i] for i in row))


dot_print(("a", "b", "c"))
