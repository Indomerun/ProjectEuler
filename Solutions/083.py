import numpy as np

def getUnmarked(currentPosition, marked):
    unmarked = []
    (x, y) = currentPosition
    if (x > 0):
        if not marked[x-1, y]:
            unmarked.append((x-1, y))
    if (x < size-1):
        if not marked[x+1, y]:
            unmarked.append((x+1, y))
    if (y > 0):
        if not marked[x, y-1]:
            unmarked.append((x, y-1))
    if (y < size-1):
        if not marked[x, y+1]:
            unmarked.append((x, y+1))
    return unmarked

def nextPos(toVisit, distance):
    minDistance = 10**10
    for idx, pos in enumerate(toVisit):
        if distance[pos[0], pos[1]] < minDistance:
            minDistance = distance[pos[0], pos[1]]
            nextPosIdx = idx
            nextPos = pos
    toVisit.pop(nextPosIdx)
    return nextPos

a = [[int(number) for number in numberString.split(',')] for numberString in open("../Data/data_083.txt").read().split('\n')]
size = len(a)
marked = np.zeros((size, size), dtype=bool)
distance = np.matrix(a)

start = (0, 0)
goal = (size-1, size-1)

currentPos = start
marked[currentPos[0], currentPos[1]] = True
toVisit = []
while currentPos != goal:
    neighbours = getUnmarked(currentPos, marked)
    for pos in neighbours:
        distance[pos[0], pos[1]] += distance[currentPos[0], currentPos[1]]
        marked[pos[0], pos[1]] = True
        toVisit.append(pos)
    currentPos = nextPos(toVisit, distance)

print(distance[goal[0], goal[1]])
