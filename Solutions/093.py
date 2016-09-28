from operator import add, sub, mul
from operator import truediv as div
import itertools

greatestLength = 0
for combination in itertools.combinations(range(1, 10), 4):
    numbers = set()
    for n in itertools.permutations(combination):
        for op in itertools.product([add, mul, sub, div], repeat=3):
            # (a.b).(c.d)
            number = op[0](op[1](n[0], n[1]), op[2](n[2], n[3]))
            if int(number) == number and number > 0:
                numbers.add(int(number))
            # ((a.b).c).d
            number = op[0](op[1](op[2](n[0], n[1]), n[2]), n[3])
            if int(number) == number and number > 0:
                numbers.add(int(number))

        i = 0
        while i+1 in numbers:
            i += 1

        if i > greatestLength:
            greatestLength = i
            answer = combination
print(greatestLength, answer)
