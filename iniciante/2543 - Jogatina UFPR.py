while True:
    try:
        num, identificador = (int(x) for x in input().split())
        counter = 0
        for c in range(num):
            ident_a,jogo = (int(y) for y in input().split())
            if ident_a == identificador and jogo == 0:
                counter += 1
        print(counter)

    except EOFError:
        break
