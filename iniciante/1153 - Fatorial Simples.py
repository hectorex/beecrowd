n = int(input())
n1 = 0
total = 1
lista = []
while n1 != n:
    n1 += 1
    lista.append(n1)

for c in range(len(lista)-1):
    total += total*lista[c]

print(total)
    