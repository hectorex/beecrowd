ca,ba,pa = [int(x) for x in input().split()]
cr,br,pr = [int(x) for x in input().split()]
total = 0
if ca >= cr:
    pass
else:
    total += cr-ca
if ba >= br:
    pass
else:
    total += br-ba
if pa >= pr:
    pass
else:
    total += pr-pa

print(total)
