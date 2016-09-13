limit = 2000000
marked = [0] * limit
value = 3
s = 2
while value < limit:
    if marked[value] == 0:
        s += value
        i = value
        while i < limit:
            marked[i] = 1
            i += value
    value += 2
print(s)