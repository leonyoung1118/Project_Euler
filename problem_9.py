def triplet(a, b, c):
    default = False
    if  a ** 2 + b ** 2 == c ** 2:
        default =  True
    return default

for m in range(1, 500):
    for n in range(m, 500):
        for q in range(n, 500):
            if triplet(m, n, q) == True and m + n + q ==1000:
                print(m * n * q)


