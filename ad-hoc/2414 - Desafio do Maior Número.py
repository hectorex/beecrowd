maiorvalor = 0
lista = [int(x) for x in input().split()]
for item in lista:
    if item > maiorvalor:
        maiorvalor = item

print(maiorvalor)
