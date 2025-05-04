valores = []
menor = 9999999999999999999999999999999999999
for c in range(int(input())):
    p,g = [float(x) for x in input().split()]
    val_por_kg = p/g
    valores.append(val_por_kg)
for valor in valores:
    if valor < menor:
        menor = valor

print(f"{(1000*menor):.2f}")