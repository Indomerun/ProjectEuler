number = 600851475143
primes = []
i = 2
while i < number/2+1:
    if number % i == 0:
        primes.append(i)
        number /= i
    else:
        i += 1
primes.append(number)
print(primes)
