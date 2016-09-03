import math
def factorialSum(n):
    sum = 0
    while n != 0:
        sum += math.factorial(n % 10)
        n //= 10
    return sum

limit = 100000
s = 0
for i in range(3,limit):
    if factorialSum(i) == i:
        s += i
        print(i)
print(s)