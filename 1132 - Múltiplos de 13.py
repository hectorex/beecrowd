x = int(input())
y = int(input())
valorfinal = 0


if x%13 != 0:
    valorfinal += x

if y%13 != 0:
    valorfinal += y


if x < y:
    for c in range(x+1,y):
        if c%13 != 0:
            valorfinal += c

    print(valorfinal)
else:
    for c in range(y+1,x):
        if c%13 != 0:
            valorfinal += c

    print(valorfinal)
