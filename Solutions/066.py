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

def getFraction(seq):
    (num, denom) = (1, seq[-1])
    for i in range(len(seq) - 1)[::-1]:
        if i != 0:
            (num, denom) = (denom, seq[i] * denom + num)
        else:
            (num, denom) = (num + seq[i] * denom, denom)
    return num, denom

Dmax = 1000
xMax = 0
answer = 0
for D in range(1,Dmax+1):
    sqrt_D = math.sqrt(D)
    if int(sqrt_D)**2 != D:
        a = int(sqrt_D)
        parameters = (a, -a, 1, 1)
        seq = [parameters[0]]
        x, y = getFraction(seq)
        while x**2 - D*y**2 != 1:
            parameters = nextNumber(D, sqrt_D, parameters)
            seq.append(parameters[0])
            x, y = getFraction(seq)
        if xMax < x:
            xMax = x
            answer = D
print(answer)
