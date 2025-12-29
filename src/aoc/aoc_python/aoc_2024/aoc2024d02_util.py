from aoc_shared.aoc_tools import load_input

def verify_report(report):
    increasing = all(1 <= report[i] - report[i - 1] <= 3 for i in range(1, len(report)))
    decreasing = all(1 <= report[i - 1] - report[i] <= 3 for i in range(1, len(report)))
    return increasing or decreasing

def read_input_file(is_test):
    reports = []

    lines = load_input(2024, 2, 1, is_test)
    for line in lines:
        # Strip whitespace and split the line
        values = list(map(int, line.strip().split()))
        reports.append(values)

    return reports
