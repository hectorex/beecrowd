salario = float(input())

if salario <= 2000.00:
    imposto = "Insento"

elif salario <= 3000.00:
    imposto = (salario - 2000.01)*0.08

elif salario <= 4500.00:
    imposto = (1000.00)*0.08 + ((salario - 3000.01))*0.18

elif salario > 4500.00:
    imposto = (1000.00/100.00)*8 + (4500.00-salario)*18

print(imposto)
