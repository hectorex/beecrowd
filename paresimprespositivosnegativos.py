a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0

def par_impar(valor):
    global impar
    global par

    if valor % 2 == 0: 
         
        par += 1

        
    else:
        
        impar += 1
        

def positivo_negativo(valorpn):
    global positivo
    global negativo

    if valorpn > 0 and valorpn != 0:
        
        positivo += 1
    
    elif valorpn == 0:
        pass
        
    else:
        negativo += 1
   

        

    
par_impar(a)
par_impar(b)
par_impar(c)
par_impar(d)
par_impar(e)

positivo_negativo(a)
positivo_negativo(b)
positivo_negativo(c)
positivo_negativo(d)
positivo_negativo(e)

print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")

# VERSÃO ANDRE ABAIXO

'''

par = 0
imp = 0
pos = 0
neg = 0

for i in range(5):
    numero = int(input(""))
    if numero % 2 == 0:
        par += 1
    
    if numero % 2 !=0:
        imp += 1

    if numero > 0:
        pos += 1

    if numero < 0:
        neg += 1

print (f"{par} valor(es) par(es)")
print (f"{imp} valor(es) impar(es)")
print (f"{pos} valor(es) positivo(s)")
print (f"{neg} valor(es) negativo(s)")

'''
