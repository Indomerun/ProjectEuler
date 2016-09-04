import math

def P(n):
    return n*(3*n-1)//2

def isPentagonal(num):
    return (1 + math.sqrt(1 + 24*num)) % 6 == 0

limitJ = 10000
limitI = 2000
found = False
for j in range(1,limitJ):
    for i in range(1, limitI):
        if isPentagonal(P(j+i) - P(j)) & isPentagonal(P(j+i) + P(j)):
            print(P(j+i) - P(j))
            found = True
            break
    if found:
        break