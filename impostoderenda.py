# CONSEGUIIIIIIIIIIII --------- ABAIXO SOLUTION

salario = float(input())

if salario <= 2000.00:
    imposto = "Isento"

elif salario <= 3000.00:
    imposto = (salario-2000)*0.08

elif salario <= 4500.00:
    imposto = (1000)*0.08 + (salario-3000)*0.18

elif salario > 4500.00:
    imposto = (1000)*0.08 + (1500)*0.18 + (salario-4500)*0.28


if imposto != "Isento":
    print(f"R$ {imposto:.2f}")
else:
    print(imposto)

    #ABAIXO ERROS/TESTES

    
# salario = float(input())

# if salario <= 2000.00:
#     imposto = "Insento"

# elif salario <= 3000.00:
#     imposto = (salario-1000)*0.08

# elif salario <= 4500.00:
#     imposto = (salario-2000)*0.08 + (salario-3000)*0.18

# elif salario > 4500.00:
#     imposto = (salario-2000)*0.08 + (salario-3000)*0.18 + (salario-4500)*0.28


# if imposto != "Insento":

#     print(f"{imposto:.2f}")
# else:
#     print(imposto)



