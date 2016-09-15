import numpy as np

limit = 100

matrix = np.ones((limit+1,limit+1),int)
for i in range(1, limit+1):
    for j in range(2, limit+1):
        if i - j >= 0:
            matrix[i, j] = matrix[i, j-1] + matrix[i-j, j]
        else:
            matrix[i, j] = matrix[i, j-1]

answer = matrix[limit, limit-1]
print(answer)