faculty = 100
limit = 2*faculty
numberList = [0]*limit
numberList[0] = 1

for i in range(1,faculty+1):
    for j in range(0,limit):
        numberList[j] *= i
    for j in range(0,limit):
        if numberList[j] >= 10:
            numberList[j+1] += (numberList[j]-numberList[j]%10)//10
            numberList[j] %= 10
print(sum(numberList))
