descart = int(input())
valores = [int(x) for x in input().split()]

mult_2 = 0
mult_3 = 0
mult_4 = 0
mult_5 = 0

for c in range(len(valores)):
    if valores[c]%2 == 0:
        mult_2 += 1
    if valores[c]%3 == 0:
        mult_3 += 1
    if valores[c]%4 == 0:
        mult_4 += 1
    if valores[c]%5 == 0:
        mult_5 += 1

print(f"{mult_2} Multiplo(s) de 2\n{mult_3} Multiplo(s) de 3\n{mult_4} Multiplo(s) de 4\n{mult_5} Multiplo(s) de 5")