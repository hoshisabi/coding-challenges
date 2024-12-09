def read_input_file(filename):
    left_list = []
    right_list = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and split the line
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    return left_list, right_list
