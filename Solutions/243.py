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

primeLimit = 100
primes = sieve8(primeLimit)

fraction = 15499/94744
n = 1
f = 1
frac = 1
i = -1
while frac >= fraction:
    i += 1
    n *= primes[i]
    f *= (1-1/primes[i])
    frac = n*f/(n-1)

n //= primes[i]
f /= (1-1/primes[i])
for num in range(2,primes[i]):
    frac = f * num*n/(n*num-1)
    if frac < fraction:
        print(num*n)
        break