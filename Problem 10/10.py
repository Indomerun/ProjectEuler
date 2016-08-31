"""Obs!! Slow as fuck"""

def isPrime(number, primeList):
    for i in primeList:
        if i >= number/2+1:
            return True
        if number % i == 0:
            return False

i = 1
primeList = [2]
number = 3
while number < 2000000:
    if isPrime(number, primeList):
        primeList.append(number)
    number += 2
    print(number)
print(sum(primeList))