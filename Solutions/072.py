limit = 10**6
marked = [False] * (limit+1)
phi = [i for i in range(limit+1)]
answer = 0
for i in range(2, limit+1):
    if not marked[i]:
        for j in range(i, limit+1, i):
            phi[j] = (phi[j]//i)*(i - 1)
            marked[j] = True
    answer += phi[i]
print(answer)
