import numpy as np

a = [[int(number) for number in numberString.split(',')] for numberString in open("../Data/data_082.txt").read().split('\n')]
size = len(a)

matrix = np.matrix(a)
matrix2 = matrix.copy()

for column in range(1, size):
    for row in range(size):
        smallest = 10**10
        for alt in range(size):
            if alt <= row:
                alternative = (matrix[alt, column-1] + matrix[alt:row, column].sum())
                if alternative < smallest:
                    smallest = alternative
            else:
                alternative = (matrix[alt, column-1] + matrix[row+1:alt+1, column].sum())
                if alternative < smallest:
                    smallest = alternative
        matrix2[row, column] += smallest
    matrix = matrix2.copy()

print(matrix[:, -1].min())
