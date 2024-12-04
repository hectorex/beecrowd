empates = 0
vencegremio = 0
vencerinter = 0
grenais = 1
inter,gremio = [int(x) for x in input().split(" ")]

if inter > gremio: 
    vencerinter += 1

elif gremio > inter: 
    vencegremio += 1

else: 
    empates += 1

print("Novo grenal (1-sim 2-nao)")
novogrenal = int(input(""))

while novogrenal == 1:
    grenais += 1
    inter,gremio = [int(x) for x in input().split(" ")]
    if inter > gremio: 
        vencerinter += 1
    elif gremio > inter: 
        vencegremio += 1
    else: 
        empates += 1
    print("Novo grenal (1-sim 2-nao)")
    novogrenal = int(input(""))

if vencegremio > vencerinter:
    vencedor = "Gremio venceu mais"
elif vencerinter > vencegremio:
    vencedor = "Inter venceu mais"
else:
    vencedor = "Nao houve vencedor"

print(f"{grenais} grenais\nInter:{vencerinter}\nGremio:{vencegremio}\nEmpates:{empates}\n{vencedor}")

