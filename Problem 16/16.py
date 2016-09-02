import math

powOf2 = 1000
limit = int(math.log10(2)*powOf2)+1
numberList = [0]*limit
numberList[0] = 1

for i in range(0,powOf2):
    for j in range(0,limit):
        numberList[j] *= 2
    for j in range(0,limit):
        if numberList[j] >= 10:
            numberList[j+1] += (numberList[j]-numberList[j]%10)//10
            numberList[j] %= 10
print(sum(numberList))