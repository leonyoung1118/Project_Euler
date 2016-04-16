def gcd(m,n):
    if m<n:
        m, n = n, m
    while True:
        m,n = n,m % n
        if n == 0:
            return m
result = 2
def lcd(m,n):
    return m * n / gcd(m,n)
for i in range(3,21):
    result = lcd(i, result)
print(result)