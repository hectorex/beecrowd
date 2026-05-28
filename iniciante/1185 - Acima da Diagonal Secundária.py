#1185 - Acima da Diagonal Secundária

matriz = []
char = input()
total = 0.0

for c in range(12):
    matriz.append([float(input()) for _ in range(12)])

for j, line in enumerate(matriz):
    for i, valor in enumerate(line):
        if i + j < 11:
            total += valor

if char == 'M':
    total /= 66.0

print(f"{total:.1f}")

'''
index = 11
for j, line in enumerate(matriz):
    for i in range(12):
        if i < index:
            total += line[i]
    index -= 1

'''