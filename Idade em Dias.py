dias = int(input(""))

ano = 0
meses = 0

while dias >= 365:
    ano += 1
    dias -= 365

while dias >= 30:
    dias -= 30
    meses += 1 

print (f"{ano} ano(s)\n{meses} mes(es)\n{dias} dia(s)")