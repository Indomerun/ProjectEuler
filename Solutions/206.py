import math

sqrNumberStr9 = "1_2_3_4_5_6_7_8_9_0"
# ultimate digit in number has to be 0
sqrNumberStr8 = "1_2_3_4_5_6_7_8_9"
# penultimate digit in number is 3 or 7

def isAnswer(n):
    str_n = str(n)
    i = 1
    while i < 9:
        if str_n[-1-2*i] != sqrNumberStr8[-1-2*i]:
            return False
        i += 1
    return True

sqrNumberStr = sqrNumberStr8
minSqr = int(sqrNumberStr.replace('_', '0'))
maxSqr = int(sqrNumberStr.replace('_', '9'))

minNum = math.sqrt(minSqr)
maxNum = math.sqrt(maxSqr)

lastNumbers = []
for i in range(1,250):
    if (str(i**2%1000)[0] == '8') & (str(i**2)[-1] == '9'):
        lastNumbers.append(i)

i = int(minNum)
i -= i % 1000

period = len(lastNumbers)
idx = 0
i += lastNumbers[idx]
while i < int(maxNum):
    if isAnswer(i**2):
        answer = i*10
        break
    i -= lastNumbers[idx]
    idx += 1
    idx %= period
    if idx == 0:
        i += 250
    i += lastNumbers[idx]

print(answer, answer**2)


"""
i = int(minNum)
i += 3 - i % 10
while i < int(maxNum):
    if isAnswer(i**2):
        answer = i*10
        break
    if i % 10 == 3:
        i += 4
    else:
        i += 6
print(answer, answer**2)
"""