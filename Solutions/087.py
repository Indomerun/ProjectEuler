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

limit = 50000000
marked = [False]*limit
primesList = sieve8(int(numpy.sqrt(limit)))

squares = [i**2 for i in primesList if i**2 < limit]
cubes = [i**3 for i in primesList if i**3 < limit]
quads = [i**4 for i in primesList if i**4 < limit]

count = 0
for quad in quads:
    for cube in cubes:
        tmpNumber = quad+cube
        if tmpNumber >= limit:
            break
        for square in squares:
            number = tmpNumber + square
            if number >= limit:
                break
            if not marked[number]:
                marked[number] = True
                count += 1
print(count)
