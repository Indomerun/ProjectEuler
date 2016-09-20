cardValue = {'2': 2,'3': 3, '4': 4,'5': 5, '6': 6,'7': 7, '8': 8,'9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def getLowestValue(hand):
    values = [card[0] for card in hand]
    sortedValues = sorted(values, key=lambda x: cardValue[x])
    return sortedValues[0]

def getHighestValue(hand):
    values = [card[0] for card in hand]
    sortedValues = sorted(values, key=lambda x: cardValue[x])
    return sortedValues[-1]

def isStraight(hand):
    values = [card[0] for card in hand]
    sortedValues = sorted(values, key=lambda x: cardValue[x])
    highest = sortedValues[-1]
    if (sortedValues[-1] == 'A') & (sortedValues[0] == '2'):
        for i in range(3):
            if cardValue[sortedValues[i+1]] != cardValue[sortedValues[i]]+1:
                return False, highest
        highest = '5'
    else:
        for i in range(4):
            if cardValue[sortedValues[i+1]] != cardValue[sortedValues[i]]+1:
                return False, highest
    return True, highest

def isFlush(hand):
    for card in hand:
        if card[-1] != hand[0][-1]:
            return False
    return True

def calcValueDict(hand):
    valueDict = {}
    for card in hand:
        try:
            valueDict[card[0]] += 1
        except KeyError:
            valueDict[card[0]] = 1
    return valueDict

def getMultiples(valueDict):
    multiples = []
    nPairs = 0
    for value in valueDict:
        if valueDict[value] == 2:
            nPairs += 1
            if nPairs == 1:
                multiples.append((1, value))
                firstPairValue = value
            if nPairs == 2:
                if valueDict[value] < valueDict[firstPairValue]:
                    multiples.remove((1, firstPairValue))
                    multiples.append((1, value))
                    multiples.append((2, firstPairValue))
                else:
                    multiples.append((2, value))
        if valueDict[value] == 3:
            multiples.append((3, value))
        if valueDict[value] == 4:
            multiples.append((6, value))
    return multiples

def getHandRank(hand):
    ranks = [(0, getHighestValue(hand))]
    straight, highestValue = isStraight(hand)
    if straight:
        ranks.append((4, highestValue))
    flush = isFlush(hand)
    if flush:
        ranks.append((5, 0))
    if straight and flush:
        for rank in ranks:
            if rank[0] == 4:
                ranks.append((8, rank[1]))
                if getLowestValue(hand) == 'T':
                    ranks.append((9, rank[1]))
                break
    valueDict = calcValueDict(hand)
    ranks = ranks + getMultiples(valueDict)
    sortedRanks = sorted(ranks, key=lambda x: x[0], reverse=True)
    return sortedRanks

def compareHands(hand1, hand2):
    rank1 = getHandRank(hand1)
    rank2 = getHandRank(hand2)
    n1 = len(rank1)
    n2 = len(rank2)
    for idx in range(n1):
        if rank1[idx][0] > rank2[idx][0]:
            return 1
        elif rank1[idx][0] == rank2[idx][0]:
            if cardValue[rank1[idx][1]] > cardValue[rank2[idx][1]]:
                return 1
            if cardValue[rank1[idx][1]] < cardValue[rank2[idx][1]]:
                return -1
        if rank1[idx][0] < rank2[idx][0]:
            return -1
        if idx == n1-1:
            if n1 > n2:
                return 1
            elif n1 == n2:
                return 0
            elif n2 > n1:
                return -1



games = [[card for card in line.split(' ')] for line in open("../Data/data_054.txt").read().split('\n')]
nGames = len(games)

p1Wins = 0
p2Wins = 0
for i in range(nGames):
    hand1 = games[i][:5]
    hand2 = games[i][5:]
    gameResult = compareHands(hand1, hand2)
    if gameResult == 1:
        p1Wins += 1
    elif gameResult == -1:
        p2Wins += 1

print(p1Wins, nGames-p1Wins-p2Wins, p2Wins)