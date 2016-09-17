from collections import Counter
ciphered = [int(i) for i in open("../Data/data_059.txt").read().split(',')]
nChars = len(ciphered)
decipheredTest = [0] * nChars

start = ord('a')
end = ord('z')
key = ''
keyLen = 3

test = ' '
for i in range(keyLen):
    for idx in range(nChars)[i::3]:
        decipheredTest[idx] = ord(test) ^ ciphered[idx]
    count = Counter(decipheredTest)
    #print(count.most_common())
    for char, nbr in count.most_common():
        if (char >= start) & (char <= end):
            key += chr(char)
            break
    print(key)

key = 'god'
deciphered = [0] * nChars
for idx in range(nChars):
    deciphered[idx] = ord(key[idx % keyLen]) ^ ciphered[idx]
print(''.join([chr(i) for i in deciphered]))
print(sum(deciphered))