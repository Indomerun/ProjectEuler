import math

limit = 1000
greatest = 0
greatestP = 0
for p in range(1,limit+1):
    s = 0
    for a in range(1,int(p/(2+math.sqrt(2)))+1):
        b = int(p*(p/2 - a)/(p - a))
        if a**2 + b**2 == (p-a-b)**2:
            s += 1
    if s > greatest:
        greatest = s
        greatestP = p

print(greatestP)