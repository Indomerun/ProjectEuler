# Using recursive (by look-up) calls of the partition function

def pentaGen(start=1):
    k = start
    while True:
        yield (k*(3*k-1))//2
        yield (k*(3*k+1))//2
        k += 1

def signGen(start=0):
    i = start
    while True:
        if i % 4 > 1:
            yield -1
        else:
            yield 1
        i += 1


divBy = 10**6
partition = [1]

n = 1
while True:
    signG = signGen()
    pentaG = pentaGen()
    partition.append(0)

    penta = next(pentaG)
    while penta <= n:
        sign = next(signG)
        partition[n] += sign * partition[n-penta]
        penta = next(pentaG)
    if partition[n] % divBy == 0:
        print(n)
        break
    n += 1
