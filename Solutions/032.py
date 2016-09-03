def isPandigital(str_n):
    for idx, i in enumerate(str_n):
        if i == '0':
            return False
        for j in str_n[idx+1:]:
            if j == i:
                return False
    return True

values = []
for i in range(1000):
    if isPandigital(str(i)):
        for j in range(10**(4-len(str(i))), 10**(5-len(str(i)))):
            if j < i:
                break
            if isPandigital(str(j)):
                product = str(i)+str(j)+str(i*j)
                if len(product) == 9:
                    if isPandigital(product):
                        append = True
                        for value in values:
                            if value == i*j:
                                append = False
                                break
                        if append:
                            values.append(i*j)

print(sum(values))