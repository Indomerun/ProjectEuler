def getNumberOfDivisors(n):
    number = n
    i = 2
    divisors = 1
    thisDivisor = 1
    while i <= number:
        if number % i == 0:
            number /= i
            thisDivisor += 1
        else:
            divisors *= thisDivisor
            thisDivisor = 1
            i += 1
    divisors *= thisDivisor
    return divisors

numberOfDivisors = 1
triangleNumber = 1
i = 1
while numberOfDivisors < 500:
    i += 1
    triangleNumber += i
    numberOfDivisors = getNumberOfDivisors(triangleNumber)

print(triangleNumber)
