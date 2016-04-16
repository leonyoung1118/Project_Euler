def lpf(x):
    lpf = 2
    while (x > lpf):
        if (x % lpf == 0):
            x = x / lpf
            lpf = 2
        else:
            lpf += 1
    print(x)

print(lpf(600851475143))