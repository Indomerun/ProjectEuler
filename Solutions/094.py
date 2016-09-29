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

def get_a_h_L(x, y):
    tmp = (2 * x + 1)
    if tmp % 3 == 0:
        a = (2 * x + 1) // 3
        L = 3*a + 1
    else:
        a = (2 * x - 1) // 3
        L = 3*a - 1
    h = y
    return a, h, L

maxL = 10**9

n = 3
sqrt_n = math.sqrt(n)
if int(sqrt_n)**2 != n:
    a = int(sqrt_n)
    parameters = (a, -a, 1, 1)
    seq = [parameters[0]]
    x1, y1 = getFraction(seq)
    while x1**2 - n*y1**2 != 1:
        parameters = nextNumber(n, sqrt_n, parameters)
        seq.append(parameters[0])
        x1, y1 = getFraction(seq)

x, y = x1*x1 + n*y1*y1, x1*y1 + y1*x1
a, h, L = get_a_h_L(x, y)
s = 0
while L <= maxL:
    s += L
    x, y = x1*x + n*y1*y, x1*y + y1*x
    a, h, L = get_a_h_L(x, y)
print(s)
