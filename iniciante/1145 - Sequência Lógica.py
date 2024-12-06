x,y = [int(u) for u in input().split(" ")]
for c in range(1,y+1):
    if c%x == 0:
        print(c)
    else:
        print(c,end=" ")