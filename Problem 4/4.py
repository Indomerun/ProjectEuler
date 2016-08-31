biggestPalindrome = 0
for i in range(1, 1000)[::-1]:
    for j in range(1, 1000)[::-1]:
        number = i * j
        numberString = str(number)
        isPalindrome = False
        for k in range(0, len(numberString)/2):
            if numberString[-1-k] != numberString[k]:
                isPalindrome = False
                break
            else:
                isPalindrome = True
        if isPalindrome & (number > biggestPalindrome):
            biggestPalindrome = number
    if i**2 < biggestPalindrome:
        break

print(biggestPalindrome)
