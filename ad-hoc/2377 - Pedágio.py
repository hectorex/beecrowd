a,b = [int(x) for x in input().split()]
d,f = [int(y) for y in input().split()]

qntd_pedagios = a//b
print((qntd_pedagios*f) + (a*d))