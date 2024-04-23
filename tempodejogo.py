split = input().split(" ")

a, b = map(int, split)

duracao = 0

if  a == b:
    duracao = 24

while a != b:
    a += 1
    duracao += 1
    if a == 24:
        # duração += 1
        a = 0
    else:
        continue


print(f"O JOGO DUROU {duracao} HORA(S)")
