for c in range(int(input())):
    nmr = int(input())
    soma = 0
    for i in range(1,nmr-1):
        if nmr%i == 0:
            soma += i
    if soma == nmr:
            print(f"{nmr} eh perfeito")
    else: print(f"{nmr} nao eh perfeito")
