limit = 100
uniqueTerms = []
for i in range(2, limit+1):
    for j in range(2, limit+1):
        if i**j not in uniqueTerms:
            uniqueTerms.append(i**j)
print(len(uniqueTerms))
