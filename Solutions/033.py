totalNum = 1
totalDenom = 1
totalFraction = 1
for num in range(10,100):
    for denom in range(num+1,100):
        if (num%10 != 0) & (denom%10 != 0):
            naiveFraction = 0
            if str(num)[0] == str(denom)[0]:
                naiveFraction = int(str(num)[1]) / int(str(denom)[1])
            elif str(num)[1] == str(denom)[1]:
                naiveFraction = int(str(num)[0]) / int(str(denom)[0])
            elif str(num)[0] == str(denom)[1]:
                naiveFraction = int(str(num)[1]) / int(str(denom)[0])
            elif str(num)[1] == str(denom)[0]:
                naiveFraction = int(str(num)[0]) / int(str(denom)[1])
            if naiveFraction == num/denom:
                totalNum *= num
                totalDenom *= denom
                totalFraction *= naiveFraction
                print("Whaat!?")
                print(num, denom)
print(totalNum, totalDenom, totalFraction)