def isPandigital(str_n):
    for idx, i in enumerate(str_n):
        if i == '0':
            return False
        for j in str_n[idx+1:]:
            if j == i:
                return False
    return True

limit = 100000//2
answer = 0
for i in range(1, limit):
    j = 1
    tmp = ''
    while len(tmp) < 9:
        tmp += str(i*j)
        j += 1
    if len(tmp) == 9:
        if isPandigital(tmp):
            if int(tmp) > answer:
                answer = int(tmp)
print(answer)
