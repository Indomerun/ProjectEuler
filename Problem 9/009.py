done = False
for a in range(1,1000/2):
    for b in range(1,1000/2):
        if 1000*(a+b) - a*b == 500000:
            done = True
            print("Found it!")
            break
    if done:
        break
print(a*b*(1000-a-b))
