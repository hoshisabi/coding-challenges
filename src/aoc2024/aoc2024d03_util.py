
def read_input_file(filename):
    lines = []
    with open(filename, 'r') as file:
        lines.extend(iter(file))
    return lines
