for c in range(int(input())):
    rsp = "Bazinga!"
    sheldon,raj = (str(a) for a in input().split(" "))
    if sheldon == raj:
        rsp = "De novo!"
    elif sheldon == "tesoura" and (raj == "lagarto" or raj == "papel"):
        rsp = "Bazinga!"
    elif sheldon == "papel" and (raj == "pedra" or raj == "Spock"):
        rsp = "Bazinga!"
    elif sheldon == "pedra" and (raj == "lagarto" or raj == "tesoura"):
        rsp = "Bazinga!"
    elif sheldon == "lagarto" and (raj == "Spock" or raj == "papel"):
        rsp = "Bazinga!"
    elif sheldon == "Spock" and (raj == "tesoura" or raj == "pedra"):
        rsp = "Bazinga!"
    else:
        rsp = "Raj trapaceou!"
    print(f"Caso #{c+1}: {rsp}")
