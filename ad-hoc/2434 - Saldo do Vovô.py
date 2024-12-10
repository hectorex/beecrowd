
a,b = [int(x) for x in input().split()]
menorvalor = b
for c in range(a):
    x = int(input())
    b += x
    if b < menorvalor:
        menorvalor = b
print(menorvalor)