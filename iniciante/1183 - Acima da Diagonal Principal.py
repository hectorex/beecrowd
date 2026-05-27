#1183 - Acima da Diagonal Principal

char = input()

matriz = []
total = 0.0
for i in range(12):
    matriz.append([float(input()) for _ in range(12)])

index = 0
for line in matriz:
    for y in range(12):
        if y > index:
            total += line[y]
    index += 1

if char == 'M':
    total /= 66

print(f"{total:.1f}")