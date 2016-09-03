side_length = 1001
n_max = side_length**2

s = 1
i = 1
period = 2
while i < n_max:
    i += period
    s += i
    i += period
    s += i
    i += period
    s += i
    i += period
    s += i
    period += 2

print(s)
