def is_pandigital(num_str):
    return set(num_str) == set("123456789")

def concatenated_product(x, n):
    return ''.join(str(x * i) for i in range(1, n + 1))

def largest_pandigital():
    largest = 0
    final_x = 0
    final_n = 0
    # we know it must be >1, so that means it has to be concatenation of two numbers
    # largest POSSIBLE is 987654321 --> divide it up in half (as string) and larger is 98765
    # so we can use this as our theoretical max (though its most likely MUCH smaller)
    for x in range(1, 98765):
        for n in range(2, 10):
            product = concatenated_product(x, n)
            if len(product) > 9:
                break
            if len(product) == 9 and is_pandigital(product):
                largest = max(largest, int(product))
                final_x = x
                final_n = n
                print(
                    "Found new largest: ",
                    largest,
                    " x=",
                    final_x,
                    " n=",
                    [i + 1 for i in range(final_n)],
                )
    return largest, final_x, final_n

result, x, n = largest_pandigital()
print("The largest 1 to 9 pandigital 9-digit number is:", result, " x=", x, " n=", [i+1 for i in range(n)])
