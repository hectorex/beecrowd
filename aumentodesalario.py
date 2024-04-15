sala = float(input())

if sala >= 0.0 and sala <= 400.00:
    salanew = (sala/100)*15
    soma = salanew + sala
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {salanew:.2f}")
    print("Em percentual: 15 %")

elif sala >= 400.01 and sala <= 800.00:
    salanew = (sala/100)*12
    soma = salanew + sala
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {salanew:.2f}")
    print("Em percentual: 12 %")

elif sala >= 800.01 and sala <= 1200.00:
    salanew = (sala/100)*10
    soma = salanew + sala
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {salanew:.2f}")
    print("Em percentual: 10 %")

elif sala >= 1200.01 and sala <= 2000.00:
    salanew = (sala/100)*7
    soma = salanew + sala
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {salanew:.2f}")
    print("Em percentual: 7 %")

elif sala > 2000.00:
    salanew = (sala/100)*4
    soma = salanew + sala
    print(f"Novo salario: {soma:.2f}")
    print(f"Reajuste ganho: {salanew:.2f}")
    print("Em percentual: 4 %")



