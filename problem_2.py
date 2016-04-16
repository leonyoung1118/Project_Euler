fib1, fib2 = 0, 1
total = 0
while True:
    fib1, fib2 = fib2, fib1 + fib2
    if fib2 >= 4000000:
        break
    if fib2 % 2 == 0:
        total += fib2
print(total)