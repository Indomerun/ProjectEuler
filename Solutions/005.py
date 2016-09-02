import math

answer = 1;
primes = [2,3,5,7,11,13,17,19]
maxTimes = [int(math.log10(20)/math.log10(i)) for i in primes]
for i in range(0,len(primes)):
    answer *= primes[i]**maxTimes[i]
print(answer)