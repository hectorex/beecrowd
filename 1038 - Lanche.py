cachorro = 4
x_salada = 4.50
x_bacon = 5
torrada_simples = 2
refrigerante = 1.50

splitas = input()
codigo, quantia = splitas.split(" ")


codigo = float(codigo)
quantia = float(quantia)

if codigo == 1:
    total = cachorro * quantia
    

elif codigo == 2:
    total = x_salada * quantia
    

elif codigo == 3:
    total = x_bacon * quantia
    print(x_bacon,quantia,total)
    

elif codigo == 4:
    total = torrada_simples * quantia
    

elif codigo == 5:
    total = refrigerante * quantia
    

print(f"Total: R$ {total:.2f}")