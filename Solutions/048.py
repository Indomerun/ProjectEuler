limit = 1000
digits = 10
finalSum = [0] * digits
power = [0] * digits

for i in range(1,limit+1):
    power = [0] * 10
    power[0] = 1
    for exponent in range(i):
        for j in range(digits):
            power[j] *= i
        for j in range(digits):
            if j < digits-1:
                power[j+1] += (power[j]-power[j]%10)//10
            power[j] %= 10
        if sum(power)==0:
            break
    for j in range(digits):
        finalSum[j] += power[j]

for j in range(digits):
    if j < digits - 1:
        finalSum[j + 1] += (finalSum[j] - finalSum[j] % 10) // 10
    finalSum[j] %= 10
print(''.join([str(num) for num in finalSum[::-1]]))