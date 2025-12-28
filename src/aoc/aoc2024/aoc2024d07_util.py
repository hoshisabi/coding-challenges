
def read_from_file(filename):
    with open(filename, 'r') as file:
        equations = [
            (int(result), list(map(int, operands.strip().split())))
            for line in file
            for result, operands in [line.strip().split(':')]
        ]
    return equations
