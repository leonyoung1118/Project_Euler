from math import sqrt
def is_primer(n):
    default = False
    for i in range(1, int(sqrt(n) )+ 1):
        if n % i != 0:
            default = True
    return default

summa = 0
x = 1
while x < 2000000:
    if is_primer(x) == True:
        summa += x
        x += 1
print(summa)


