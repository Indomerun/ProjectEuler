limit = 1000
largestPeriod = 0
for d in range(1, limit):
    rest = 1
    decimals = {}
    i = 0
    while True:
        (decimal, rest) = ((10*rest)//d, (10*rest) % d)
        if (decimal, rest) in decimals:
            period = i-decimals[(decimal, rest)]
            break
        else:
            decimals[(decimal, rest)] = i
        i += 1
    if period > largestPeriod:
        largestPeriod = period
        answer = d
print(answer)
