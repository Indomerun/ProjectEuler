limit = 1000000
number = [0]*limit
i = 1
digit = 1
while digit <= limit:
    for j in range(len(str(i))):
        if digit-1+j < limit:
            number[digit-1+j] = int(str(i)[j])
    digit += len(str(i))
    i += 1

answer = 1
for i in range(7):
    answer *= number[10**i-1]
print(answer)
