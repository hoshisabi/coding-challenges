def get_combo(operand, reg_a, reg_b, reg_c):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return reg_a
        case 5:
            return reg_b
        case 6:
            return reg_c
        case 7:
            return -1


def execute_instruction(program, instruction_pointer, reg_a, reg_b, reg_c, out):
    halt = False
    new_instruction_pointer = instruction_pointer + 2
    if len(program) < instruction_pointer + 2:
        halt = True
    else:
        opcode = program[instruction_pointer]
        literal_operand = program[instruction_pointer + 1]
        combo_operand = get_combo(literal_operand, reg_a, reg_b, reg_c)

        if combo_operand == -1:
            halt = True
        else:
            match opcode:
                case 0:  # adv
                    num = reg_a
                    den =  2 ** combo_operand
                    reg_a = num // den
                case 1:  # bxl
                    reg_b ^= literal_operand
                case 2:  # bst
                    reg_b = combo_operand % 8
                case 3:  # jnz
                    if reg_a != 0:
                        new_instruction_pointer = literal_operand
                case 4:  # bxc
                    reg_b ^= reg_c
                case 5:  # out
                    out += [combo_operand % 8]
                case 6:  # bdv
                    num = reg_a
                    den = 2 ** combo_operand
                    reg_b = num // den
                case 7:  # cdv
                    num = reg_a
                    den = 2 ** combo_operand
                    reg_c = num // den
    return halt, new_instruction_pointer, reg_a, reg_b, reg_c, out


def read_file(filename):
    with open(filename, 'r') as file:
        reg_a_string = file.readline().strip().split(":")[1]
        reg_b_string = file.readline().strip().split(":")[1]
        reg_c_string = file.readline().strip().split(":")[1]
        _ = file.readline().strip()
        program_string = file.readline().strip().split(":")[1]
    return (int(reg_a_string)), (int(reg_b_string)), (int(reg_c_string)), (list(map(int, program_string.split(","))))
