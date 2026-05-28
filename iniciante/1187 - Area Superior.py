# 1187 - Área Superior

matriz = []

ope = input()
total = 0.0

for i in range(12):
    matriz.append([float(input()) for _ in range(12)])

cont = 0
for i, line in enumerate(matriz):
    for j, number in enumerate(line):
        if j > cont and j < 11-cont:
            total += number
    cont +=1

if ope == 'M':
    total /= 30

print(f'{total:.1f}')
