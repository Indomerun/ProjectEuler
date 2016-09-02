def isPrime(number, primeList):
    for i in primeList:
        if i >= number/2+1:
            return True
        if number % i == 0:
            return False

i = 1
primeList = [2]
number = 3
while i < 10001:
    if isPrime(number, primeList):
        i += 1
        primeList.append(number)
    number += 1
print(len(primeList), primeList[-1])

