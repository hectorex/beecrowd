a = int(input())
while a != 0:
    pnts_mary = 0
    pnts_j = 0
    lista = [int(x) for x in input().split()]
    for item in lista:
        if item == 0:
            pnts_mary += 1
        else:
            pnts_j += 1
    print(f"Mary won {pnts_mary} times and John won {pnts_j} times")
    a = int(input())
