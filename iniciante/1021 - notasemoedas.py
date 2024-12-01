val = float(input())

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0

moedas1 = 0
moedas05 = 0
moedas025 = 0
moedas010 = 0
moedas005 = 0
moedas001 = 0


while val >= 2.00:
    while val >= 100.00:
        val -= 100.00
        notas100 += 1

    while val >= 50.00 and val < 100.00:
        val -= 50.00
        notas50 += 1

    while val >= 20.00 and val < 50.00:
        val -= 20.00
        notas20 += 1

    while val >= 10.00 and val < 20.00:
        val -= 10.00
        notas10 += 1

    while val >= 5.00 and val < 10.00:
        val -= 5.00
        notas5 += 1

    while val >= 2.00 and val < 5.00:
        val -= 2.00
        notas2 += 1
        
while val >= 0.01:

    while val >= 1.00:
        val -= 1.00
        moedas1 += 1

    while val >= 0.50 and val < 1.00 :
      
        val -= 0.50
        moedas05 += 1
 
    while val >= 0.25 and val < 0.50:
      
        val -= 0.25
        moedas025 += 1

    while val >= 0.10 and val < 0.25:
      
        val -= 0.10
        moedas010 += 1

    while val >= 0.05 and val < 0.10:
        val -= 0.05
        moedas005 += 1

    while val >= 0.001:
        val -= 0.01
        moedas001 += 1
        

print(f"NOTAS:\n{notas100} nota(s) de R$ 100.00\n{notas50} nota(s) de R$ 50.00\n{notas20} nota(s) de R$ 20.00\n{notas10} nota(s) de R$ 10.00\n{notas5} nota(s) de R$ 5.00\n{notas2} nota(s) de R$ 2.00\nMOEDAS:\n{moedas1} moeda(s) de R$ 1.00\n{moedas05} moeda(s) de R$ 0.50\n{moedas025} moeda(s) de R$ 0.25\n{moedas010} moeda(s) de R$ 0.10\n{moedas005} moeda(s) de R$ 0.05\n{moedas001} moeda(s) de R$ 0.01")



