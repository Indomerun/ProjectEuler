def isPalindromic(str_n):
    for i in range(len(str_n)//2):
        if str_n[i] != str_n[-i-1]:
            return False
    return True

limit = 1000000
s = 0
for i in range(limit):
    if isPalindromic(str(i)) & isPalindromic(str(bin(i))[2:]):
        s += i
print(s)