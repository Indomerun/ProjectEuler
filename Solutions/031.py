coins = [1, 2, 5, 10, 20, 50, 100, 200]
ncoins = len(coins)
limit = 200

matrix = [[1]*ncoins for i in range(limit+1)]
for i in range(1, limit+1):
    for j in range(1, ncoins):
        if i - coins[j] >= 0:
            matrix[i][j] = matrix[i][j-1] + matrix[i-coins[j]][j]
        else:
            matrix[i][j] = matrix[i][j-1]
print(matrix[limit])
