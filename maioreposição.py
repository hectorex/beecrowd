maiorvalors = 0
posicao = 0

for c in range(101):
    valor = int(input())
    if valor > maiorvalors:
        maiorvalors = valor
        posicao = c
    else:
        continue

print(maiorvalors)
print(posicao)