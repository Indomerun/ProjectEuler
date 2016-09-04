import math

def permute(n, iterList):
    n = list(n)
    for i in iterList:
        if int(n[i-1]) < int(n[i]):
            break
    for j in iterList:
        if(j >= i) & (int(n[j]) > int(n[i-1])):
            break
    n[j], n[i-1] = n[i-1], n[j]
    n[i:] = (n[i:])[::-1]
    return ''.join(n)


permutation = '0123456789'
length = len(permutation)
iterList = range(length)[::-1]
primesList = [2,3,5,7,11,13,17]
s = 0
for i in range(math.factorial(10)):
    works = True
    for j in range(7):
        if (int(permutation[1+j:4+j]) % primesList[j]) != 0:
            works = False
            break
    if works:
        s += int(permutation)
    permutation = permute(permutation, iterList)
print(s)