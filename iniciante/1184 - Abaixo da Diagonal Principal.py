#1184 - Abaixo da Diagonal Principal
char = input()

matriz = []
total = 0.0
for i in range(12):
    matriz.append([float(input()) for _ in range(12)])

for i, line in enumerate(matriz):
    for j in range(12):
        if j < i:
            total += line[j]

if char == 'M':
    total /= 66

print(f"{total:.1f}")