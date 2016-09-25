def getNRectangles(nRows, nCols):
    nRectangles = 0
    for i in range(nRows):
        for j in range(nCols):
            nRectangles += (nRows - i) * (nCols - j)

    return nRectangles

nRows = 0
nCols = 0
smallest = 10**10
answer = 0
while nCols >= nRows:
    nRows += 1
    nCols = 1
    current = getNRectangles(nRows, nCols)
    while current < 2000000:
        previous = current
        nCols += 1
        current = getNRectangles(nRows, nCols)
    if abs(previous-2000000) <= abs(current-2000000):
        if abs(previous-2000000) < smallest:
            smallest = abs(previous-2000000)
            answer = nRows*(nCols-1)
    else:
        if abs(current-2000000) < smallest:
            smallest = abs(current-2000000)
            answer = nRows*nCols
print(answer)
