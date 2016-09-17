attempts = [i for i in open("../Data/data_079.txt").read().split('\n')]

passCodeL = ''
passCodeR = ''

left = {}
right = {}
for nbr in attempts:
    for i in range(2):
        for j in range(i+1, 3):
            try:
                right[nbr[i]][int(nbr[j])] = 1
            except KeyError:
                right[nbr[i]] = [0] * 10
                left[nbr[i]] = [0] * 10
                right[nbr[i]][int(nbr[j])] = 1
            try:
                left[nbr[j]][int(nbr[0])] = 1
            except KeyError:
                right[nbr[j]] = [0] * 10
                left[nbr[j]] = [0] * 10
                left[nbr[j]][int(nbr[i])] = 1

for i in range(len(right.keys())):
    for key in right.keys():
        if sum(right[key]) == 0:
            passCodeR = key + passCodeR
            for otherKey in right:
                right[otherKey][int(key)] = 0
            del right[key]
            break

for i in range(len(left.keys())):
    for key in left.keys():
        if sum(left[key]) == 0:
            passCodeL = passCodeL + key
            for otherKey in left:
                left[otherKey][int(key)] = 0
            del left[key]
            break

if passCodeR == passCodeL:
    print(passCodeR)
else:
    print("Something went wrong!")
