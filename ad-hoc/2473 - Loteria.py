splitas = input().split(" ")
a,b,c,d,e,f = map(int,splitas)
splitas = input().split(" ")
a2,b2,c2,d2,e2,f2 = map(int,splitas)

lista1 = [a,b,c,d,e,f]


acertos = 0

resposta = ""

for c in range(len(lista1)): 
    if lista1[c] == a2 or lista1[c] == b2 or lista1[c] == c2 or lista1[c] == d2 or lista1[c] == e2 or lista1[c] == f2:
        acertos += 1

if acertos < 3: resposta = "azar"
if acertos == 3: resposta = "terno"
if acertos == 4: resposta = "quadra"
if acertos == 5: resposta = "quina"
if acertos == 6: resposta = "sena"

print(resposta)

