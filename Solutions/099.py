import math
a = [[int(number) for number in numberString.split(',')] for numberString in open("../Data/data_099.txt").read().split('\n')]
size = len(a)

greatestExp = 0
answer = 0
for n in range(size):
    if math.log10(a[n][0])*a[n][1] > greatestExp:
        greatestExp = math.log10(a[n][0]) * a[n][1]
        answer = n+1
print(answer)
