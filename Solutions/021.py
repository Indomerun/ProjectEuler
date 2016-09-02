import math

def d(n):
    return sum(getDivisors(n))+1

def getDivisors(n):
    sqrt_n = int(math.sqrt(n))
    divisors = []
    for i in range(2, sqrt_n+1):
        if n%i == 0:
            if i == sqrt_n:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(n//i)
    return divisors

numbers = [0] * 10001
for i in range(0,10001):
    numbers[i] = d(i)

amicable = []
for i in range(0,10001):
    if numbers[i] <= 10000:
        if numbers[numbers[i]] == i:
            if numbers[i] != i:
                amicable.append(i)
                amicable.append(numbers[i])
                numbers[numbers[i]] = 0

print(sum(amicable))
