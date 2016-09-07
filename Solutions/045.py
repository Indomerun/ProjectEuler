import math

def H(start=1):
    n = start
    while True:
        yield n*(2*n-1)
        n += 1

def isPentagonal(num):
    return (1 + math.sqrt(1 + 24*num)) % 6 == 0

def isTriangle(num):
    return (-1 + math.sqrt(1 + 8*num)) % 2 == 0

for num in H(start=143):
    if isPentagonal(num) & isTriangle(num):
        print(num)
        break
