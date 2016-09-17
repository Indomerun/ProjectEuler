import math

# Euclidean algorithm for GCD (Greatest Common Denominator)
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def number(sqrt_n, parameters):
    (a, b, c, d) = parameters
    return (d*sqrt_n+b)/c

def nextNumber(n, sqrt_n, parameters):
    (a, b, c, d) = parameters
    a = int(1/number(sqrt_n, parameters))
    e = (d**2)*n - b**2
    (b, c, d) = -(c * b + a * e), e, c * d
    f = gcd(b, d)
    f = gcd(f, c)
    return (a, b//f, c//f, d//f)

limit = 10000
s = 0
for n in range(2, limit+1):
    sqrt_n = math.sqrt(n)
    if int(sqrt_n)**2 != n:
        a = int(sqrt_n)
        parameters = (a, -a, 1, 1)
        parameters = nextNumber(n, sqrt_n, parameters)
        parameters_1 = parameters
        parameters = nextNumber(n, sqrt_n, parameters)
        i = 1
        while parameters != parameters_1:
            parameters = nextNumber(n, sqrt_n, parameters)
            i += 1
        s += i % 2
print(s)
