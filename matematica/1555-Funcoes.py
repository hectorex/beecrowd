for c in range(int(input())):
    x, y = map(int, input().split())
    rafa = (3*x)**2+(y**2)
    beto = 2*(x**2)+(5*y)**2
    carlo = -100*x + y**3
    if (rafa > beto and rafa > carlo):
        print("Rafael ganhou")
    elif (beto > rafa and beto > carlo):
        print("Beto ganhou")
    elif (carlo > rafa and carlo > beto):
        print("Carlos ganhou")