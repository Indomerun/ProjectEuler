count = 0
n = 1
while len(str(9**n)) == n:
    for a in range(1, 10):
        if len(str(a**n)) == n:
            count += 1
    n += 1
print(count)
