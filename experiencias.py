coeio = 0
rat = 0
sap = 0

n = int(input())


for c in range(n):
    splitas = input().split(" ")
    qntd, anmal = map(str, splitas)
    qntd = int(qntd)
    if anmal == 'C':
        coeio += qntd
    elif anmal == 'R':
        rat += qntd
    elif anmal == 'S':
        sap += qntd
total = coeio+rat+sap
porcent3 = (rat/total)*100
porcent2 = (coeio/total)*100
porcent1 = (sap/total)*100
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coeio}")
print(f"Total de ratos: {rat}")
print(f"Total de sapos: {sap}")
print(f"Percentual de coelhos: {porcent2:.2f} %")
print(f"Percentual de ratos: {porcent3:.2f} %")
print(f"Percentual de sapos: {porcent1:.2f} %")


