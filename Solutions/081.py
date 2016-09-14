import numpy as np
a = [[int(number) for number in numberString.split(',')] for numberString in open("../Data/data_081.txt").read().split('\n')]
size = len(a)
matrix = np.matrix(a)

for row in range(size):
    for column in range(size):
        if (row == 0) | (column == 0):
            if column != 0:
                matrix[row, column] += matrix[row, column-1]
            elif row != 0:
                matrix[row, column] += matrix[row-1, column]
        else:
            matrix[row, column] += min(matrix[row-1, column], matrix[row, column-1])
print(matrix[-1, -1])
