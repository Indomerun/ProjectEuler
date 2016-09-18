def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

a = 1
b = 3
c = 1
d = 2

limit = 12000

s = 0
for q in range(2, limit+1):
    p_min = (a*q)//b + 1
    p_max = (c*q-1)//d
    for p in range(p_min, p_max+1):
        if gcd(p, q) == 1:
            s += 1
print(s)