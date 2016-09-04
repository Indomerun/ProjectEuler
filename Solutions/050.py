limit = 1000000
marked = [0] * limit
value = 3
primes = [2]
isPrime = [False] * (limit+1)
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

s = 0
maxi = 0
while s < limit:
    s += primes[maxi]
    maxi += 1

done = False
for length in range(1,maxi)[::-1]:
    for i in range(maxi-length):
        if isPrime[sum(primes[i:length+i])]:
            done = True
            break
    if done:
        break
if done:
    print(length, sum(primes[i:length + i]))
