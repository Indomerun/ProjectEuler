limit = 100000
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

consecutive = 4
maximum = 1
for i in range(consecutive-1):
    maximum *= primes[i]
done = False
distincts = [0] * consecutive
i = maximum-1
while not done:
    i += 1
    num = i
    k = 0
    distincts[0] = 0
    while (primes[k] <= num) & (primes[k] <= i//maximum) & (distincts[0] < consecutive):
        if num % primes[k] == 0:
            num //= primes[k]
            distincts[0] += 1
            while num % primes[k] == 0:
                num //= primes[k]
        k += 1
    done = True
    for distinct in distincts:
        if distinct != consecutive:
            done = False
    distincts[1:] = distincts[0:consecutive-1]
    distincts[0] = 0

print(i+1-consecutive)