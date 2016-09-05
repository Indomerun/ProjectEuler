limit = 1000000
marked = [0] * limit
value = 3
primes = [2]
isPrime = [False] * (limit+1)
isPrime[2] = True
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

def rightTruncate(n):
    return int(str(n)[:-1])

def leftTruncate(n):
    return int(str(n)[1:])

filteredPrimes = [num for num in primes if ('0' not in str(num)) & ('2' not in str(num)[1:]) & ('4' not in str(num)) & ('6' not in str(num)) & ('8' not in str(num))]

answer = 0
for prime in filteredPrimes:
    truncated = prime
    if prime < 10:
        truncPrime = False
    else:
        truncPrime = True
    while truncated//10 != 0:
        truncated = rightTruncate(truncated)
        if not isPrime[truncated]:
            truncPrime = False
            break
    truncated = prime
    if truncPrime:
        while truncated // 10 != 0:
            truncated = leftTruncate(truncated)
            if not isPrime[truncated]:
                truncPrime = False
                break
    if truncPrime:
        answer += prime
print(answer)
