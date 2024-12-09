def verify_report(report):
    increasing = all(1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report)))
    decreasing = all(1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report)))
    return increasing or decreasing

def read_input_file(filename):
    reports = []

    with open(filename, 'r') as file:
        for line in file:
            # Strip whitespace and split the line
            values = list(map(int, line.strip().split()))
            reports.append(values)

    return reports
