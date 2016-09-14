def intToList(n):
    return list(map(int, str(n)))

def listToInt(n):
    return int(''.join(map(str, n)))

def hasDouble(num):
    for idx, n in enumerate(str(num)):
        if n in str(num)[idx+1:]:
            return True
    return False

limit = 1000000
marked = [0] * limit
isPrime = [False] * limit
primesList = []
value = 3
while value < limit:
    if marked[value] == 0:
        isPrime[value] = True
        if hasDouble(value):
            primesList.append(value)
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

def getMultiples(n):
    nList = intToList(n)
    multiples = []
    indices = []
    for idx, i in enumerate(nList):
        if idx not in indices:
            tmp = []
            jdx = idx
            for j in nList[idx:]:
                if i == j:
                    tmp.append(jdx)
                    indices.append(jdx)
                jdx += 1
            if len(tmp) >= 2:
                multiples.append(tmp)
                if len(tmp) == 3:
                    multiples.append([tmp[0], tmp[1]])
                    multiples.append([tmp[1], tmp[2]])
                    multiples.append([tmp[0], tmp[2]])
    return multiples

answer = 0
nPrimes = 8
for prime in primesList:
    nDigits = len(str(prime))
    multiples = getMultiples(prime)
    for indices in multiples:
        if nDigits-1 in indices:
            pass
        elif 0 in indices:
            primeSeq = intToList(prime)
            fail = 0
            i = 1
            while (fail <= 9-nPrimes) & (i <= 9):
                for idx in indices:
                    primeSeq[idx] = i
                if not isPrime[listToInt(primeSeq)]:
                    fail += 1
                i += 1
            if (fail <= 9-nPrimes):
                answer = prime
        else:
            primeSeq = intToList(prime)
            fail = 0
            i = 0
            while (fail <= 10-nPrimes) & (i <= 9):
                for idx in indices:
                    primeSeq[idx] = i
                if not isPrime[listToInt(primeSeq)]:
                    fail += 1
                i += 1
            if (fail <= 10-nPrimes):
                answer = prime
        if answer != 0:
            break
    if answer != 0:
        break
print(answer)