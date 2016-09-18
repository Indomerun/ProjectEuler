def P(n):
    return [(n*(n + 1))//2, n**2, (n*(3*n-1))//2, n*(2*n-1), (n*(5*n-3))//2, n*(3*n-2)]

allNumbers = []
n = 0
numbers = P(n)
while numbers[0] < 10000:
    for type, value in enumerate(numbers):
        if (1000 <= value) & (value < 10000):
            allNumbers += [(type, value)]
    n += 1
    numbers = P(n)

relations = {}
for type1, value1 in allNumbers:
    for type2, value2 in allNumbers:
        if (type1 != type2) & (value1 != value2):
            if value1 % 100 == value2 // 100:
                try:
                    relations[(type1, value1)] += [(type2, value2)]
                except KeyError:
                    relations[(type1, value1)] = [(type2, value2)]

def recursiveSearch(types, values):
    if (len(types) == 6) & (values[0] // 100 == values[-1] % 100):
        print(values)
        print(sum(values))
    else:
        for type, value in relations.get((types[-1], values[-1]), []):
            if type not in types:
                recursiveSearch(types + [type], values + [value])

for type, value in relations:
    recursiveSearch([type], [value])
