import math

def nextNumberInCycle(n):
    return sum([int(i)**2 for i in str(n)])

def nextNonPermutation(n):
    nDigits = len(n)
    for idx in range(0, nDigits):
        if n[idx] != 9:
            n[idx] += 1
            for i in range(0, idx):
                n[i] = n[idx]
            return n

def nPermutations(n):
    nDigits = len(n)
    perm = math.factorial(nDigits)
    idx = 0
    while idx < nDigits-1:
        j = idx
        while n[j] == n[idx]:
            j += 1
            if j == nDigits:
                break
        perm //= math.factorial(j-idx)
        idx = j
    return perm

nDigits = 7
limit = nDigits * 9**2
marked = [-1] * (limit + 1)
marked[0] = 0
marked[1] = 0
marked[89] = 1
for i in range(1, limit+1):
    tmp = i
    while marked[tmp] == -1:
        tmp = nextNumberInCycle(tmp)
    marked[i] = marked[tmp]

sequence = [0] * nDigits
count = 0
while sequence != None:
    if marked[nextNumberInCycle(int(''.join(map(str, sequence))))] == 1:
        count += nPermutations(sequence)
    sequence = nextNonPermutation(sequence)
print(count)