impares = []
pares = []
for c in range(15):
    num = int(input())
    if len(pares) == 5:
        for i in range(len(pares)):
            print(f"par[{i}] = {pares[i]}")
        pares = []
    elif len(impares) == 5:
        for y in range(len(impares)):
            print(f"impar[{y}] = {impares[y]}")
        impares = []
    if num%2 == 0:
        pares.append(num)
    else:
        impares.append(num)



for m in range(len(impares)):
    print(f"impar[{m}] = {impares[m]}")

for l in range(len(pares)):
    print(f"par[{l}] = {pares[l]}")