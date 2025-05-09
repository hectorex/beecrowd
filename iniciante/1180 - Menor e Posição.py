p = int(input())
lista = [int(x) for x in input().split()]
menor = lista[0]
posicao = 0
for i in range (0,len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        posicao = i

print(f"Menor valor: {menor}")
print(f"Posicao: {posicao}")