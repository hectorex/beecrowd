#VERSAO GPTLIZADA:

n = int(input())
for i in range(2, n + 1, 2):
    print(f"{i}^2 =", i**2)


# MINHA VERSAO ABAIXO



n = int(input())

valor_n_de_teste = n

numeros_locos = 0


if n %2 == 0:
    variaveldecontrole = True
    while valor_n_de_teste != 0:
        valor_n_de_teste -= 2
        numeros_locos += 1
        


else:
    variaveldecontrole = False
    valor_n_de_teste -= 1
    while valor_n_de_teste != 0:
        valor_n_de_teste -= 2
        numeros_locos += 1

valor_n_de_teste_2 = 0
        

if variaveldecontrole == True:
    for c in range (numeros_locos):
        valor_n_de_teste_2 += 2
        print(f"{valor_n_de_teste_2}^{2} =",valor_n_de_teste_2**2)
else:
    for c in range (numeros_locos):
        valor_n_de_teste_2 += 2
        print(f"{valor_n_de_teste_2}^{2} =",valor_n_de_teste_2**2)
