def num2sorted(n):
    list = [int(i) for i in str(n)]
    sortedList = sorted(list, reverse=True)
    return ''.join(str(num) for num in sortedList)

sortedCubes = {}
i = 1
while True:
    num = i**3
    sortedNum = num2sorted(num)
    try:
        sortedCubes[sortedNum][0] += 1
        if sortedCubes[sortedNum][0] == 5:
            print(sortedCubes[sortedNum][1])
            break
    except KeyError:
        sortedCubes[sortedNum] = [1, num]
    i += 1


# Old solution:

def isPermutation(str_n1, str_n2):
    digits = [0] * 10
    if len(str_n1) != len(str_n2):
        return False
    for idx in range(len(str_n1)):
        digits[int(str_n1[idx])] += 1
        digits[int(str_n2[idx])] -= 1
    for value in digits:
        if value != 0:
            return False
    return True

l = 1
cubes = {l: []}
L = 0
answer = 1

i = 1
while answer == 0:
    nextNumber = str(i**3)
    if len(nextNumber) != l:
        l += 1
        cubes[l] = []
        L = 0
    cubes[l].append([nextNumber, 1])
    L += 1
#    print(i, L)
    for j in range(L-1):
        if isPermutation(cubes[l][-1][0], cubes[l][j][0]):
            cubes[l][j][1] += 1
            cubes[l][-1][1] += 1
            if cubes[l][j][1] == 5:
                answer = cubes[l][j][0]
                break
    i += 1
#print(answer)