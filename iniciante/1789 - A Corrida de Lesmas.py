while True:
    nivel = 1
    try:
        l = int(input())
        lista = [int(x) for x in input().split()]
        for velocidade in lista:
            if velocidade >= 10 and velocidade  < 20:
                nivel = 2
            if velocidade >= 20:
                nivel = 3
                break
        print(nivel)
    except EOFError:
        break