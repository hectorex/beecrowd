while True:
    nota1 = float(input())
    while nota1 < 0 or nota1 > 10:
        print("nota invalida")
        nota1 = float(input())

    nota2 = float(input())
    while nota2 < 0 or nota2 > 10:
        print("nota invalida")
        nota2 = float(input())

    print(f"media = {((nota1+nota2)/2):.2f}")
    
    print("novo calculo (1-sim 2-nao)")
    novo_calculo = int(input())
    if novo_calculo == 2: exit()
    while novo_calculo < 1 or novo_calculo > 2:
        print("novo calculo (1-sim 2-nao)")
        novo_calculo = int(input())
        if novo_calculo == 1: continue
        if novo_calculo == 2: exit()