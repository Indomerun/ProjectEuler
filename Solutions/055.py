def isPalindromic(str_n):
    for i in range(len(str_n)//2):
        if str_n[i] != str_n[-i-1]:
            return False
    return True

def nextNumber(n):
    return int(str(n)) + int(str(n)[::-1])

limit = 10000
iterationLimit = 50
iteration = range(iterationLimit)
count = 0
for number in range(1, limit):
    currentNumber = number
    for i in iteration:
        currentNumber = nextNumber(currentNumber)
        if isPalindromic(str(currentNumber)):
            break
    if not isPalindromic(str(currentNumber)):
        count += 1
print(count)