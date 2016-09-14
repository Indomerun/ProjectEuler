import numpy

def sieve8(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]

limit = 2*10**9

primesList = sieve8(limit)
primeIdx = 0

currentNumber = 1
period = 2
nPrimes = 0
nDiags = 1
iterationsList = range(4)

while True:
    for i in iterationsList:
        currentNumber += period
        nDiags += 1
        while primesList[primeIdx] < currentNumber:
            primeIdx += 1
        if primesList[primeIdx] == currentNumber:
            nPrimes += 1
            primeIdx += 1
    if nPrimes/nDiags > 0.1:
        period += 2
    else:
        break
side_length = period+1
print(nPrimes/nDiags, side_length)