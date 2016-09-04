import math

def isPandigital(str_n):
    for idx, i in enumerate(str_n):
        if i == '0':
            return False
        for j in str_n[idx+1:]:
            if j == i:
                return False
    return True

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

def antiPermute(n, iterList):
    n = list(n)
    for i in iterList:
        if int(n[i-1]) > int(n[i]):
            break
    for j in iterList:
        if(j >= i) & (int(n[j]) < int(n[i-1])):
            break
    n[j], n[i-1] = n[i-1], n[j]
    n[i:] = (n[i:])[::-1]
    return ''.join(n)

def isPrime(n,listOfPrimes):
    sqrt_n = math.sqrt(n)
    for i in listOfPrimes:
        if i > sqrt_n:
            break
        if n % i == 0:
            return False
    return True

limit = int(math.sqrt(1000000000))+1
marked = [0] * limit
value = 3
primes = [2]
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

startPermutation = '987654321'
answerFound = False
for i in range(9):
    permutation = startPermutation[i:]
    length = len(permutation)
    iterList = range(length)[::-1]
    for j in range(math.factorial(9)):
        if isPrime(int(permutation), primes):
            answerFound = True
            break
        permutation = antiPermute(permutation, iterList)
    if answerFound:
        break
print(permutation)
