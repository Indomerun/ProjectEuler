limit = 1000000
marked = [0] * limit
value = 3
isPrime = [False] * limit
isPrime[2] = True

primes = [2]
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

def rotate(n):
    str_n = str(n)
    return int(str_n[1:]+str_n[0])

s = 0
for i in range(limit):
    if isPrime[i]:
        isRot = True
        n = i
        for j in str(i):
            if (not isPrime[n]) | (len(str(n)) != len(str(i))):
                isRot = False
                break
            n = rotate(n)
        if isRot:
            #print(i)
            s += 1
print(s)