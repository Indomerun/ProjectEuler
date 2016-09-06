def isPermutation(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    digits = [0] * 10
    if len(str_n1) != len(str_n2):
        return False
    for idx in range(len(str_n1)):
        digits[int(str_n1[idx])] += 1
        digits[int(str_n2[idx])] -= 1
    for value in digits:
        if value != 0:
            return False
    return True




limit = 10000
marked = [0] * limit
value = 3
primes = [2]
isPrime = [False] * (limit+1)
isPrime[2] = True
while value < limit:
    if marked[value] == 0:
        primes.append(value)
        isPrime[value] = True
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2

filteredPrimes = [num for num in primes if num > 1000 & num < 10000]
for idx, i in enumerate(filteredPrimes):
    if i > 1000:
        for j in filteredPrimes[idx+1:]:
            k = i + 2*(j-i)
            if k > 10000:
                break
            if isPrime[k]:
                if isPermutation(i, j) & isPermutation(j, k):
                    print(i,j,k)
