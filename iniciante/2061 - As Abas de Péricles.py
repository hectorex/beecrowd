a,b = [int(x) for x in input().split()]
for c in range(b):
    rsp = input()
    if rsp == "fechou":
        a += 1
    elif rsp == "clicou":
        a -= 1

print(a)