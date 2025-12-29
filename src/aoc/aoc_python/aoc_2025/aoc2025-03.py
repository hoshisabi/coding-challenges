from aoc_shared.aoc_tools import load_input

def get_data(fname):
    lines = None
    with open(fname) as f:
        lines = f.readlines()
    return lines

def solve_line(number_list, number_of_digits):
    line_sum = 0
    partial_list = number_list
    for digit in range(number_of_digits):
        end_pos = number_of_digits - digit - 1
        f = max(partial_list[:len(partial_list)-end_pos])
        f_idx = partial_list.index(f)
        partial_list = partial_list[f_idx+1:]
        line_sum *= 10
        line_sum += f
        print(f"    {number_of_digits} - {digit} - {f} - {f_idx} - {partial_list} - {line_sum}")
    return line_sum
def solve(data, number_of_digits):
    data_sum = 0
    for line in data:
        numbers = [int(x) for x in line.strip()]
        data_sum += solve_line(numbers, number_of_digits)
    return data_sum

if __name__ == '__main__':
    data = load_input(2025, 3, is_test=True)

    part1 = solve(data, 2)
    part2 = solve(data, 12)
    print("Day 3")
    print(f"part 1: {part1}")
    print(f"part 2: {part2}")
