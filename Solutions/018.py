a = [[int(number) for number in numberString.split(' ')] for numberString in open("../Data/data_018.txt").read().split('\n')]

for i in range(1, len(a)):
    a[i][0] += a[i - 1][0]
    a[i][-1] += a[i - 1][-1]
    for j in range(1, i):
        a[i][j] += max(a[i-1][j-1:j+1])

print(max(a[-1]))


