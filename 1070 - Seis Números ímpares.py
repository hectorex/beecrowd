x = int(input())

if x %2 != 0:

    for c in range(6):
        print(x)
        x += 2
else:
    x += 1
    for c in range(6):
        print(x)
        x += 2