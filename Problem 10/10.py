"""
#Obs!! Slow as fuck
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
"""

limit = 2000000
marked = [0] * limit
value = 3
s = 2
while value < limit:
    if marked[value] == 0:
        s += value
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2
print(s)