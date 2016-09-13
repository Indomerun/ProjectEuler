import math
def C(n,r):
    return math.factorial(n)/(math.factorial(r) * math.factorial(n-r))

number = 0
for n in range(23,100+1):
    for r in range(1,n+1):
        if C(n,r) > 1000000:
            number += 1
print(number)