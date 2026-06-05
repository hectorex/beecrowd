hour = input()
while hour != EOFError:
    try:
        a,b = map(int, hour.split(":"))
        if a >= 7:
            atraso = 60-(60-b) + (a-7)*60

        else:
            atraso = 0
        print("Atraso maximo:",atraso)
        hour = input()
    except EOFError:
        break