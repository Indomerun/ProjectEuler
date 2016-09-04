import math

def H(n):
    return n*(2*n-1)

def isPentagonal(num):
    return (1 + math.sqrt(1 + 24*num)) % 6 == 0

def isTriangle(num):
    return (-1 + math.sqrt(1 + 8*num)) % 2 == 0

found = False
i = 1
while not found:
    num = H(i)
    if isPentagonal(num) & isTriangle(num):
        print(num)
        if num > 40755:
            break
    i += 1
