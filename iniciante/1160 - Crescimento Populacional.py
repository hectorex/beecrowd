for c in range(int(input())):
    pA,pB,cA,cB = [float(x) for x in input().split()]
    pA = int(pA)
    pB = int(pB)
    anos = 0
    while anos < 101 and pB >= pA:
        anos += 1
        pA += pA*(cA/100)
        pA = int(pA) #to transformando essa porra aqui pq se não fica somando uns decimais na conta,
        #então, eu sempre transforma eles em int pra garantir q não vao ter decimais a mais por causa da divisão
        pB += pB*(cB/100)
        pB =  int(pB)  #caso queira ver na prática, comentar a linha 9 e a linha 12 e colocar para printar pA e pB, verá os decimais a partir da 2 casa atrapalhando a conta.
        
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")
