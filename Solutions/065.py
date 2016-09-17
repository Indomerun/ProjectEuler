def a(k):
    if k == 0:
        return 2
    elif (k+1) % 3 == 0:
        return 2 * (k+1) // 3
    else:
        return 1

# Valid for seqNbr > 1
seqNbr = 100
(num, denom) = (1, a(seqNbr-1))
for k in range(seqNbr-1)[::-1]:
    if k != 0:
        (num, denom) = (denom, a(k)*denom + num)
    else:
        (num, denom) = (num + a(k)*denom, denom)
print(sum([int(i) for i in str(num)]))
