case = 1

while True:
    vet = []
    try:
        n = int(input())
        if n == 0:
            vet.append(n)
            print(f"Caso {case}: {len(vet)} numero")
        else:
            vet.append(0)

        if n != 0:
            for c in range(0, n+1):
                for y in range(c):
                    vet.append(c)
            print(f"Caso {case}: {len(vet)} numeros")

        for index, i in enumerate(vet):
            if index == len(vet)-1:
                print(i, end ="")
            else:
                print(i, end=" ")
            
        print()

        case += 1
        print()
        
    except EOFError:
        break