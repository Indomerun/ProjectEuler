from itertools import combinations

def allSquares(c1, c2):
    for x, y in squares:
        if not((x in c1 and y in c2) or (x in c2 and y in c1)):
            return False
    return True
squares = []
for i in range(1, 10):
    if i**2 % 10 != 9:
        squares.append((i**2 // 10, i**2 % 10))
    else:
        squares.append((i**2 // 10, 6))

digits = [i for i in range(10)]
digits[9] = 6
c = 0
for c1 in combinations(digits, 6):
    for c2 in combinations(digits, 6):
        if allSquares(c1, c2):
            c += 1
print(c//2)
