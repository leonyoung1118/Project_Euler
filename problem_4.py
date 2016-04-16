def palindromic(i):
    if int(str(i)[::-1]) == i:
        return True

num = 0
for a in range(999, 99, -1):
    for b in range(a, 99 ,-1):
        product = a * b
        
        if palindromic(product) and  product > num:
            num = product

print(num)