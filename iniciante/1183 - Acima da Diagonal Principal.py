#1183 - Acima da Diagonal Principal
char = input()

matriz = []
total = 0.0
for i in range(12):
    matriz.append([float(input()) for _ in range(12)])

for i, line in enumerate(matriz):
    for j in range(12):
        if j > i:
            total += line[j]

if char == 'M':
    total /= 66

print(f"{total:.1f}")

'''
GAMBIARRA Q ESTAVA NO LUGAR DO ENUMERATE
index = 0
for line in matriz:
    for y in range(12):
        if y > index:
            total += line[y]
    index += 1

'''