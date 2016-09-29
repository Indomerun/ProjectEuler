import math
# M = l1 >= l2 >= l3

limit = 10**6
count = 0
l1 = 0
while count < limit:
    l1 += 1
    for l23 in range(2, 2*l1):
        hyp = math.sqrt(l1**2 + l23**2)
        if hyp == int(hyp):
            if l23 > l1:
                count += l1 - (l23+1)//2 + 1
            else:
                count += l23//2
print(l1)
