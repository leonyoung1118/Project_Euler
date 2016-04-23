def positive(n):
    loop = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            loop += 1
        else:
            n = 3 * n + 1
            loop += 1
    return loop

value = 0
for i in range(1, 1000000):
    if positive(i) > value:
        value = positive(i)
        print(i)


print(value)