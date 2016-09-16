# Using Euclid's formula for generating all unique Pythagorean triples

# Euclidean algorithm for GCD (Greatest Common Denominator)
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

limit = 1500000
counts = [0] * (limit+1)

n = 1
while 2*(n+1)*(n+1+n) <= limit:
    m = n+1
    L = 2*m*(m+n)
    while L <= limit:
        if (gcd(m, n) == 1) & ((m-n) % 2 == 1):
            k = 1
            while k*L <= limit:
                counts[k*L] += 1
                k += 1
        m += 1
        L = 2*m*(m+n)
    n += 1
answer = sum([1 for i in counts if i == 1])
print(answer)
