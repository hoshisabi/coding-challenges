# contains 4 digits
# not start with 0

def is_four_digit(pin: str) -> bool:
    """Check if a string represents a four-digit number.

    Args:
        pin: The input string.

    Returns:
        True if the string is a valid four-digit number, False otherwise.
    """
    return len(pin) == 4


def not_start_with_zero(pin: str) -> bool:
    """Check if a PIN starts with zero.

    Args:
        pin: The input PIN.

    Returns:
        True if the PIN starts with zero, False otherwise.
    """
    return pin[0] != '0'


def not_sequential_or_consecutive_digits(pin: str) -> bool:
    for i in range(len(pin) - 1):
        this_digit = int(pin[i])
        next_digit = int(pin[i + 1])
        if this_digit in [next_digit + 1, next_digit - 1, next_digit]:
            return False
    return True


def all_checks(pin: str) -> bool:
    return is_four_digit(pin) and not_start_with_zero(pin) and not_sequential_or_consecutive_digits(pin)


import itertools

all_pins = valid_pins = 0
for a, b, c, d in itertools.product(range(9), range(9), range(9), range(9)):
    pin = f"{a}{b}{c}{d}"
    all_pins += 1
    if all_checks(pin):
        valid_pins += 1

print(all_pins, valid_pins, 100 * (valid_pins / all_pins))
