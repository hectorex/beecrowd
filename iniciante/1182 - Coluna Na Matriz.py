#1182 - Coluna na Matriz
columNum = int(input())
char = input()

matriz = []

for i in range(12):
    matriz.append([float(input()) for _ in range(12)])

total = 0.0

for line in matriz:
    total += line[columNum]

if (char == 'M'):
    total /= 12

print(f"{total:.1f}")

#codigo antigo a baixo

'''
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
'''
