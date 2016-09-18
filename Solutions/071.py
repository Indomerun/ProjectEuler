limit = 10**6
c = 3
d = 7

currentBest = 0
for b in range(1, limit+1):
    a = (b*c-1)//d
    f = a/b
    if f > currentBest:
        currentBest = f
        answer = (a, b)
print(answer)
