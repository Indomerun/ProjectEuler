limit = 10**6
power = 5

i = 2
s = 0
while i < limit:
    tmp = 0
    n = i
    while n != 0:
        tmp += (n % 10)**power
        n //= 10
    if tmp == i:
        s += i
    i += 1
print(s)