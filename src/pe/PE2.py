def fib(a):
    x, y = 0, 1
    for i in range(a):
        print(f"{x}, {y}")
        if x % 2 == 0:
            yield x
        x, y = y, x + y


i = 1
tot = 0
ret = 0

while ret <= 4_000_000:
    tot += fib(i)
    print(f"So far at {i}, sum is {tot}")
    i += 1

print(f"Stopped at {i} and sum was {tot}")
