#for a in range(1, 10):
#    for b in range(10):
#        ab = (a * 10) + b
#        cab = ab ** 2
#        if (cab % 100) == ab:
#            print(ab)

a = 1
b = 1
ab = 1
cab = 0
while (cab % 100) != ab:
    if b == 9:
        a += 1
        b = 0
    else:
        b += 1
        ab = (a * 10) + b
        cab = ab ** 2
else:
    print(ab)