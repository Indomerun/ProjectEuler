def permute(n, iterList):
    for i in iterList:
        if (n[i-1]) < (n[i]):
            break
    for j in iterList:
        if(j >= i) & ((n[j]) > (n[i-1])):
            break
    n[j], n[i-1] = n[i-1], n[j]
    n[i:] = (n[i:])[::-1]
    return n

permutation = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(permutation)
iterList = range(length)[::-1]
for i in range(999999):
    permutation = permute(permutation, iterList)

print(''.join([str(num) for num in permutation]))
