x = float(input())
lista = [x]
print(f"N[0] = {x:.4f}")
for c in range(1,100):
    lista.append(lista[c-1]/2)
    print(f"N[{c}] = {lista[c]:.4f}")

