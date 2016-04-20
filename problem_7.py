def is_prime(n):
    default = True
    for i in range(2, n):
        if n % i == 0:
            default = False
    return default


def prime10001(n):
    u = 2
    num = 1
    while True:
        if is_prime(u)== True:
            print (u, num)
            num += 1
        if u > n:
            break
        u += 1
    return u

print (prime10001(10001))
