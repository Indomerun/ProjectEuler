import math

def fraction():
    num = denom = 1
    while True:
        (num, denom) = (2 * denom + num, denom + num)
        yield (num, denom)

log10 = math.log(10)
f = fraction()
s = 0
for i in range(1000):
    num, denom = next(f)
    if int(math.log(num)/log10) > int(math.log(denom)/log10):
        s += 1
print(s)
