a = int(input())
total = 0
for c in range(a):
    d,e = (int(x) for x in input().split())
    if d == 1001:
        total += e*1.50
    elif d == 1002:
        total += e*2.50
    elif d == 1003:
        total += e*3.50
    elif d == 1004:
        total += e*4.50
    elif d == 1005:
        total += e*5.50
print(f"{total:.2f}")