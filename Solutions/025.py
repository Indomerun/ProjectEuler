import math
GoldenRatio = (math.sqrt(5) + 1) / 2

previous = 0
next = 1
numberOfDigits = 1
for i in range(2, 5000):
    tmp = next
    next += previous
    previous = tmp

    if next >= 10:
        next /= 10
        previous /= 10
        numberOfDigits += 1

    if numberOfDigits == 1000:
        break
print(i)
