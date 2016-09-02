def nextPosition(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1

limit = 1000000
distance = [0] * limit
biggest=0
number=0
for i in range(1,limit):
    position = i
    if distance[i] == 0:
        while position != 1:
            if nextPosition(position) < limit:
                if distance[nextPosition(position)] != 0:
                    distance[i] += distance[nextPosition(position)]
                    position = 1
                else:
                    position = nextPosition(position)
                    distance[i] += 1
            else:
                position = nextPosition(position)
                distance[i] += 1
        distance[i] += 1
    if distance[i] > biggest:
        biggest = distance[i]
        number = i

print(number)
