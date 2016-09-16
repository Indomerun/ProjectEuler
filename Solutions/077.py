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
    return numpy.r_[2, result]

limit = 100
primes = sieve8(limit)
nPrimes = len(primes)

# row 0 has to be 1 in order to give +1 for when i is prime
# row 1 has to be 0 because 2 is the smallest prime
matrix = [[1] * nPrimes,
          [0] * nPrimes]
for i in range(2, limit+1):
    row = [0] * nPrimes
    for j in range(0, nPrimes):
        if i - primes[j] >= 0:
            row[j] = matrix[i-primes[j]][j]
            if j != 0:
                row[j] += row[j-1]
        else:
            if j != 0:
                row[j] = row[j-1]
    matrix.append(row)
    if row[-1] > 5000:
        print(i)
        break
