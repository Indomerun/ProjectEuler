def nextNumber(n, p, s, aStart):
    k = n + p - s
    if k < kLim+1:
        if p < N[k]:
            N[k] = p
        for a in range(aStart, NMax//p + 1):
            nextNumber(n+1, p*a, s+a, a)


kLim = 12000
NMax = 2*kLim
N = [NMax+1] * (kLim+1)
nextNumber(1, 1, 1, 2)

s = set()
for n in N[2:]:
    s.add(n)
print(sum(s))
