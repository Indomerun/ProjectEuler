import math

def nextNumberInCycle(n):
    return sum([math.factorial(int(i)) for i in str(n)])

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


count = 0
for nDigits in range(1,7):

    sequence = [0] * nDigits
    while sequence != None:
        i = int(''.join(map(str, sequence)))
        chain = [i]
        tmp = nextNumberInCycle(i)
        while tmp not in chain:
            chain.append(tmp)
            tmp = nextNumberInCycle(tmp)
        chainLength = len(chain)
        if chainLength == 60:
            nPerm = nPermutations(sequence)
            str_i = str(i)
            for idx in range(len(str_i)):
                n = 0
                if str_i[idx] == '0':
                    n += 1
            for j in range(n):
                nPerm //= len(str_i)-j
                nPerm *= len(str_i)-n
            count += nPerm
        sequence = nextNonPermutation(sequence)
print(count)
