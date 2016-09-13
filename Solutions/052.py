def sameDigits(num1, num2):
    num1str = str(num1)
    num2str = str(num2)
    if len(num1str) != len(num2str):
        return False
    for digit in num1str:
        if digit not in num2str:
            return False
    for digit in num2str:
        if digit not in num1str:
            return False
    return True

i = 1
answer = 0
while answer == 0:
    for j in range(2, 7):
        if not sameDigits(i, j*i):
            break
        if j == 6:
            answer = i
    i += 1
    if len(str(i*6)) > len(str(i)):
        i = 10**len(str(i))
print(answer)
