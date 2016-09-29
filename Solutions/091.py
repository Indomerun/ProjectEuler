gridMax = 50

x1 = [0, 1]
x2 = [0, 2]
count = 0
while x1[0] <= gridMax:
    while x1[1] <= gridMax:
        x2[0] = x1[0]
        x2[1] = x1[1]+1
        while x2[0] <= gridMax:
            while x2[1] <= gridMax:
                l1 = x1[0]**2 + x1[1]**2
                l2 = x2[0]**2 + x2[1]**2
                l12 = l1 + l2 - 2*x1[0]*x2[0] - 2*x1[1]*x2[1]
                l = sorted([l1, l2, l12])
                if l[0] + l[1] == l[2]:
                    count += 1
                x2[1] += 1
            x2[1] = 0
            x2[0] += 1
        x1[1] += 1
    x1[0] += 1
    x1[1] = 0
print(count)
