import math

limit = 1000000
marked = [0] * limit
value = 3
primes = [2]
isPrime = [False] * (limit+1)
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

answer = 0
for i in range(2, limit+1):
    if i % 2 != 0:
        if not isPrime[i]:
            idx = 0
            works = 0
            while primes[idx] < i:
                potentialSquare = (i-primes[idx])//2
                if int(math.sqrt(potentialSquare))**2 == potentialSquare:
                    works = 1
                    break
                idx += 1
            if works == 0:
                answer = i
                break

print(answer)
