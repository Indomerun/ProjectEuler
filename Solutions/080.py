from decimal import *
getcontext().prec = 105

n_max = 100
s = 0
for n in range(1,n_max+1):
    if int(n**0.5)**2 != n:
        s += sum([int(i) for i in str(Decimal(n).sqrt())[:101] if i != '.'])
print(s)

