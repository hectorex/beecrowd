y = int(input())

for c in range(y):
    a,b = [str(a) for a in input().split()]
    if a == "Thor" and b > "0":
        rsp = "Y"
    else:
        rsp = "N"
    print(rsp)
