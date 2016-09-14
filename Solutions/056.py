limit = 100
answer = 0
for a in range(1,limit):
    for b in range(1,limit):
        digitSum = sum([int(i) for i in str(a**b)])
        if digitSum > answer:
            answer = digitSum
print(answer)