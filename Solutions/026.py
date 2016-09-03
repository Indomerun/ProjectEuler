def nextDecimal(decimal,d):
    return (10 * decimal[1]) // d, (10 * decimal[1]) % d

limit = 10000
max_d = 999
cycles = [0] * max_d
for d in range(1,max_d+1):
    decimal1 = (1,1)
    d1 = d
    while d1 != 0:
        d1 //= 10
        decimal1 = nextDecimal(decimal1, d)
    decimal2 = nextDecimal(decimal1, d)
    period = 1
    for i in range(10000):
        done = True
        decimal1 = nextDecimal(decimal1, d)
        decimal2 = nextDecimal(decimal2, d)
        while period < limit:
            if decimal1[0] == decimal2[0]:
                break
            decimal2 = nextDecimal(decimal2, d)
            period += 1
        if period < limit:
            for j in range((1+1000//period)*period):
                decimal1 = nextDecimal(decimal1, d)
                decimal2 = nextDecimal(decimal2, d)
                if decimal1[0] != decimal2[0]:
                    done = False
                    break
            if done:
                break
        else:
            period = 1
    if (period == 1) & (decimal1[0] == 0) & (decimal2[0] == 0):
        period = 0
    cycles[d-1] = period
max_cycle = max(cycles)
for i, n in enumerate(cycles):
    if n == max_cycle:
        break
print(i+1, max_cycle)

