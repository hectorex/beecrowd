a,b = [int(x) for x in input().split()]
if a == b:
    rsp = a
elif a > b:
    rsp = a
elif b > a:
    rsp = b
print(rsp) 