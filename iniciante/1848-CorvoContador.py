gritos = 0

while gritos < 3:
    num = 0
    piscada = str(input())
    while piscada != "caw caw":
        if piscada == "--*":
            num += 1
        elif piscada == "-*-":
            num += 2
        elif piscada == "-**":
            num += 3
        elif piscada == "*--":
            num += 4
        elif piscada == "*-*":
            num += 5
        elif piscada == "**-":
            num += 6
        elif piscada == "***":
            num += 7
        elif piscada == "---":
            num += 0
        piscada = str(input())
        
    print(num)
    gritos += 1
