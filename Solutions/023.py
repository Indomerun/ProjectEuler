import math

def getDivisors(n):
    sqrt_n = math.sqrt(n)
    divisors = []
    for i in range(2, int(sqrt_n)+1):
        if n % i == 0:
            divisors.append(i)
            if i != sqrt_n:
                divisors.append(n//i)
    return divisors

limit = 28123
abundant = [False]*limit
for i in range(12, limit):
    if not abundant[i]:
        if sum(getDivisors(i))+1 > i:
            n = i
            while n < limit:
                abundant[n] = True
                n += n

abundantList = []
for i in range(limit):
    if abundant[i]:
        abundantList.append(i)

sumOfAbundant = []
non_abundant = []
for i in range(limit):
    for ab1 in abundantList:
        if ab1 > i:
            non_abundant.append(i)
            break
        if abundant[i-ab1] == 1:
            sumOfAbundant.append(i)
            break
print(sum(non_abundant))
