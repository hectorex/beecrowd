d = int(input())

pnts = 0

if d <= 800:
    pnts = 1
elif d <= 1400:
    pnts = 2
elif d <= 2000:
    pnts = 3

print(pnts)