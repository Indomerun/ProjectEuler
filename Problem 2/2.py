fib = [0, 1]
while fib[-1] < 4000000:
    fib.append(fib[-1]+fib[-2])

print(sum([x for x in fib[:-1] if (x % 2 == 0)]))
