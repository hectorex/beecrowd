x = int(input())
while x != 0:
    for c in range(1,x+1):
        if c == x:
            print(c)
        else:
            print(c,end=" ")
    x = int(input())