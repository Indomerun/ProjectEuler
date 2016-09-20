import math

def nCr(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

print(7 * (1 - nCr(60, 20)/nCr(70, 20)))
