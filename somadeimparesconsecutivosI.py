#gepetes abaixo


# Leia os valores inteiros X e Y
x = int(input())
y = int(input())

# Garanta que X seja menor que Y, se necessário
if x > y:
    x, y = y, x

# Inicialize a variável para armazenar a soma dos ímpares
soma_impares = 0

# Percorra os números entre X e Y, inclusive
for num in range(x + 1, y):
    if num % 2 != 0:
        soma_impares += num

# Imprima a soma dos ímpares
print(soma_impares)









## TENTATIVA FUCKING UMA

# x = int(input())
# y = int(input())

# valorfinal = 0


# impares = 0
# if x % 2 == 0:
#     x -= 1

#     if x > y:
#         for c in range(x,y,-2):
#             print(c)
#             valorfinal = valorfinal + c
#             print("testrlinha14")

#     else: 
#         for c in range(x,y,2):
#             valorfinal = valorfinal + c
#             print("testrlinha20")
# else:
#     if y > x:
#         for c in range(x,y,2):
#             valorfinal = valorfinal + c
#             print("testrlinha25")

#     else: 
#         for c in range(x,y,-2):
#             print(c)
#             valorfinal = valorfinal + c
#             print("testrlinha30")


# print(valorfinal)

#TENTATIVA 2 (DEU CERTO ESSA MERDA NAO SEI COMO)


x = int(input())
y = int(input())

valor_final = 0

if x == y:
        print("0")  
        exit()

elif x %2 == 0:
    x -= 1
    if x > y:
        while x != y:
            valor_final = x + valor_final
            x -= 2

    else:
         while y != x:
            valor_final = y + valor_final
            y -= 2
            
            
else:
    if x > y:
        while x != y:
            
            x -= 2
            valor_final = x + valor_final
            if x-y == 1:
                break
            
    else:
         while y != x:
            y -= 2
            valor_final = y + valor_final
            

print(valor_final)







