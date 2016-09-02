singles = ['','one','two','three','four','five','six','seven','eight','nine']
tens1 = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundreds = 'hundred'
thousands = 'onethousand'

def getText(n):
    text = ''
    if n > 1000:
        return "Too large value"
    if n >= 100:
        if n == 1000:
            return thousands
        else:
            text += singles[(n-n%100)//100]
            text += hundreds
            if n%100 != 0:
                text += 'and'
    if 10 <= n%100 & n%100 < 20:
        text += tens1[n%100-10]
    else:
        text += tens[((n-n%10)//10)%10]
        text += singles[n%10]
    return text

numberOfCharacters = 0
for i in range(1,1001):
    numberOfCharacters += len(getText(i))

print(numberOfCharacters)