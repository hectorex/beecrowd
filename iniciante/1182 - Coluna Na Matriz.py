columNum = int(input())
char = str(input())

matriz = []

for i in range(12):
    list = []
    for y in range(12):
        list.append(float(input()))
    matriz.append(list)

nums = 0.0

for p in range(len(matriz)):
    nums += matriz[p][columNum]

if (char == 'M'):
    nums /= 12

print(f"{nums:.1f}")
