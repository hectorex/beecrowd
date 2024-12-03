while True: 
    sum = 0
    m,n = [int(x) for x in input().split()]
    if m <= 0 or n <= 0 :
        break
    if m > n:
        maiornum = m
        menornum = n
    elif n > m:
        maiornum = n
        menornum = m
    for c in range(maiornum-menornum+1):
        sum += menornum+c
        print(menornum+c,end=" ")
    print(f"Sum={sum}")
        
