lista = [int(x) for x in input().split()]
for c in range(len(lista)):
    if lista[c] == 1:
        print(c+1)