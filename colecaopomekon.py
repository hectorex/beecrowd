#LINK DA QUESTÃO -- https://judge.beecrowd.com/pt/problems/view/2174

total = 151

lista = []
pokemons = []

quantos = int(input())

for c in range(quantos):
    pokemondaniel = str(input())
    lista.append(pokemondaniel)

# para cada item na lista, tera um for
for c in lista:
    if c not in pokemons:
        #se item c nao entre lista pokemons, adicionar na lista pokemons (vai ser a lista correta e sem repetições)
        pokemons.append(c) 
    
encontrados = len(pokemons)
#ver qual o tamanho ta lista, pois já que esta sem repetições, podemos so descobrir o número que equivale a sua quantidade de pokemons e o diminuir por 151 (numero total de pomekons)

print("Falta(m)",total-encontrados,"pomekon(s).")




# ----------- TUDO AQUI PRA BAIXO SAO TENTATIVAS FALHAS!!! ---------------







# # pomekonstotaL = 151

# # quantia = int(input())
# # listapomekons = []

# # for i in range(quantia):
# #     pomekon = str(input())
# #     listapomekons.append(pomekon)

# # for y in range(quantia-1):
# #     if listapomekons[y] != listapomekons[y+1]:
# #         pomekonstotaL = pomekonstotaL - 1
# #         print(y)   
# #     else:
# #         pass






# # # c = 0
# # # a = 0

# # # whilec = 0


# # # while whilec == 0:
# # #     a += 1
# # #     if listapomekons[quantia] == [quantia-a]:
# # #         c += 1
# # #         if c == quantia:
# # #             pomekonstotaL += 1
# # #             break
# # #         else:
# # #             continue



# # # if listapomekons[quantia-1] == listapomekons[quantia-2] and listapomekons[quantia-2] == listapomekons[quantia-3]:
# # #     pomekonstotaL -= 1
    
# # print(f"Falta(m) {pomekonstotaL} pomekon(s).")


# # #definindo qntd
# # quantidade = int(input())
# # #vendo qual o primeiro pmk
# # string1 = str(input())
# # #redifinindo a qntd
# # quantidade -= 1

# # #lista de pomekons
# # lista = [string1]

# # totaldepp = 151

# # for i in range(quantidade):
# #     pomekon = str(input())
# #     lista.append(pomekon)
# #     totaldepp -= 1
# #     # if pomekon in lista:
# #     #     totaldepp = totaldepp
# #     # else:
        

# # for c in range(quantidade):
# #     while quantidade != 0:
# #         if lista[c] in list:
# #             print("DEU CERTO KRL")
# #             totaldepp += 1
# #             if 

        
# controle = 0

# total = 151

# lista = []

# quantos = int(input())

# for c in range(quantos):
#     pokemondaniel = str(input())
#     lista.append(pokemondaniel)

# a = False
# i = 0
# y = 0
# penis = quantos


# while a == False:
#         if pokemondaniel[i] != pokemondaniel[y+1]:
#               penis -= 1
#               if penis == 0:
#                     break
#         else:


# # for corno in range(quantos):

# #     for b in range(quantos-1):
# #         if lista[b] != lista[b+1] and lista[b] != [b-1]:
# #             print("linha92")
# #             controle += 1
# #             if controle == quantos - 1:
# #                 print("line95")
# #                 controle = controle-controle
# #                 print(total)
# #                 total -= 1
        
        

# # print(total)

