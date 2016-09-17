data = open("../Data/data_089.txt").read().split('\n')
size = len(data)

numerals = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

def readRoman(romanNum, numerals):
    s = numerals[romanNum[0]]
    idx = 1
    while idx < len(romanNum):
        if numerals[romanNum[idx-1]] >= numerals[romanNum[idx]]:
            s += numerals[romanNum[idx]]
        else:
            s -= 2*numerals[romanNum[idx-1]]
            s += numerals[romanNum[idx]]
        idx += 1
    return s

def writeRoman(number):
    romanNum = ''
    romanNum += 'M' * (number//1000)
    number %= 1000
    romanNum += 'CM' * (number//900)
    number %= 900
    romanNum += 'D' * (number//500)
    number %= 500
    romanNum += 'CD' * (number//400)
    number %= 400
    romanNum += 'C' * (number//100)
    number %= 100
    romanNum += 'XC' * (number//90)
    number %= 90
    romanNum += 'L' * (number//50)
    number %= 50
    romanNum += 'XL' * (number//40)
    number %= 40
    romanNum += 'X' * (number//10)
    number %= 10
    romanNum += 'IX' * (number//9)
    number %= 9
    romanNum += 'V' * (number//5)
    number %= 5
    romanNum += 'IV' * (number//4)
    number %= 4
    romanNum += 'I' * number
    number %= 1
    return romanNum

initialLength = 0
compressedLength = 0
for romanNum in data:
    number = readRoman(romanNum, numerals)
    compressedNum = writeRoman(number)
    initialLength += len(romanNum)
    compressedLength += len(compressedNum)
print(initialLength-compressedLength)