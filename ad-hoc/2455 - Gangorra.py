p1,c1,p2,c2 = [int(x) for x in input().split()]
if p1*c1 == p2*c2:
    rsp = 0
elif p1*c1 > p2*c2:
    rsp = -1
else:
    rsp = 1

print(rsp)