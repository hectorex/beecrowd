tamanhosequencia = int(input())
secret = 1
listasenumeros = []

for c in range(tamanhosequencia):
    a = int(input())
    listasenumeros.append(a)

for a in range(tamanhosequencia-1):

    if listasenumeros [a] != listasenumeros[a+1]:
        secret += 1

print(secret)
