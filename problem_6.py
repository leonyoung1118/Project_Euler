sum1 = 0
for i in range(1, 101):
    num = i ** 2
    sum1 += num

sum2 = 0
for u in range(1, 101):
    sum2 += u

print(sum1)
print(sum2)
print(sum2 ** 2 - sum1)
