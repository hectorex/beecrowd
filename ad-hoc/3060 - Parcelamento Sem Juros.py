valor = int(input())
parcelas = int(input())
if valor%parcelas == 0:
    for c in range(parcelas):
        print(valor//parcelas)
else:
    resto = valor%parcelas 
    for c in range(resto):
        print((valor//parcelas)+1)
    for i in range(parcelas-resto):
        print(valor//parcelas)