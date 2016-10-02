import numpy
from copy import deepcopy

class SuDokuBoard:

    def __init__(self, initialBoard=None):
        self.elements = numpy.zeros((9, 9), dtype=int)
        self.subBoard = numpy.empty((3, 3), dtype=object)
        self.exclusives = numpy.empty((9, 9), dtype=object)
        self.nExclusives = numpy.zeros((9, 9), dtype=int)
        self.choices = numpy.empty((9, 9), dtype=object)
        self.nChoices = numpy.zeros((9, 9), dtype=int)
        for i in range(3):
            for j in range(3):
                self.subBoard[i, j] = set()
        if initialBoard is not None:
            for i in range(9):
                for j in range(9):
                    self.setElement(i, j, initialBoard[i][j])
            self.update()

    def __str__(self):
        string = ''
        for i in range(9):
            for j in range(9):
                string += str(self.elements[i, j]) + ' '
            string += '| '
            for j in range(9):
                string += str(self.nChoices[i, j]) + ' '
            string += '| '
            for j in range(9):
                string += str(self.nExclusives[i, j]) + ' '
            string += '\n'
        return string

    def copy(self):
        return deepcopy(self)

    def getElement(self, i, j):
        return self.elements[i, j]

    def setElement(self, i, j, x):
        self.elements[i, j] = x
        self.subBoard[i//3, j//3].add(x)

    def getSubBoardList(self, i, j):
        return self.subBoard[i//3, j//3].copy()

    def getChoices(self, i, j):
        return self.choices[i, j].copy()

    def singularChoiceExists(self):
        for i in range(9):
            for j in range(9):
                if self.nChoices[i, j] == 1:
                    return True
        return False

    def updateNChoices(self):
        for i in range(9):
            for j in range(9):
                self.nChoices[i, j] = len(self.choices[i, j])

    def updateChoices(self):
        for i in range(9):
            for j in range(9):
                if self.elements[i, j] == 0:
                    exclude = self.getSubBoardList(i, j)
                    for k in range(9):
                        exclude.add(self.elements[i, k])
                        exclude.add(self.elements[k, j])
                    self.choices[i, j] = [x for x in range(1, 10) if x not in exclude]
                else:
                    self.choices[i, j] = []
        self.updateNChoices()

    def getExclusives(self, i, j):
        return self.exclusives[i, j].copy()

    def singularExclusiveExists(self):
        for i in range(9):
            for j in range(9):
                if self.nExclusives[i, j] == 1:
                    return True
        return False

    def updateNExclusives(self):
        for i in range(9):
            for j in range(9):
                self.nExclusives[i, j] = len(self.exclusives[i, j])

    def updateExclusives(self):
        for i in range(9):
            for j in range(9):
                self.exclusives[i, j] = []
                for number in self.choices[i, j]:
                    c = 0
                    for k in range(3):
                        for l in range(3):
                            if number in self.choices[3*(i//3) + k, 3*(j//3) + l]:
                                c += 1
                            if c > 1:
                                break
                        if c > 1:
                            break
                    if c == 1:
                        self.exclusives[i, j].append(number)
        self.updateNExclusives()

    def update(self):
        self.updateChoices()
        self.updateExclusives()

    def choiceSolve(self):
        while True:
            c = 0
            for i in range(9):
                for j in range(9):
                    if self.nChoices[i, j] == 1:
                        if self.isValid(i, j, self.getChoices(i, j)[0]):
                            self.setElement(i, j, self.getChoices(i, j)[0])
                            c += 1
            if c == 0:
                break
            self.updateChoices()
        self.updateExclusives()

    def exclusiveSolve(self):
        for i in range(9):
            for j in range(9):
                if self.nExclusives[i, j] == 1:
                    if self.isValid(i, j, self.getExclusives(i, j)[0]):
                        self.setElement(i, j, self.getExclusives(i, j)[0])
        self.update()

    def logicalSolve(self):
        while self.singularChoiceExists() or self.singularExclusiveExists():
            self.choiceSolve()
            self.exclusiveSolve()

    def getSolution(self):
        self.update()
        self.logicalSolve()
        for i in range(9):
            for j in range(9):
                if self.getElement(i, j) == 0:
                    for number in range(1, 10):
                        if self.isValid(i, j, number):
                            newBoard = self.copy()
                            newBoard.setElement(i, j, number)
                            solution = newBoard.getSolution()
                            if solution is not None:
                                return solution
                    return None
        return self

    def isValid(self, i, j, x):
        if x not in self.elements[i, :]:
            if x not in self.elements[:, j]:
                if x not in self.subBoard[i//3, j//3]:
                    return True
        return False

rows = [[int(element) for element in line] for line in open("../Data/data_096.txt").read().split('\n') if line[0] != 'G']
games = []
for i in range(50):
    games.append(rows[9 * i:9 * (i + 1)])

s = 0
for i in range(50):
    game = games[i]
    currentBoard = SuDokuBoard(game)
    solution = currentBoard.getSolution()
    s += solution.getElement(0, 0) * 100 + solution.getElement(0, 1) * 10 + solution.getElement(0, 2)
print(s)
