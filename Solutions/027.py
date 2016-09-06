def P(a, b, n):
    return n**2 + a*n + b

limit = 100000
marked = [0] * limit
value = 3
isPrime = [False] * (limit+1)
isPrime[2] = True
while value < limit:
    if marked[value] == 0:
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

aLim = 999
bLim = 1000

iMax = 0
for a in range(-aLim, aLim+1):
    for b in range(-aLim, aLim+1):
        idx = 0
        while isPrime[P(a, b, idx)]:
            idx += 1
        if idx > iMax:
            iMax = idx
            answer = a*b
print(answer)
