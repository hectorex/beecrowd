for c in range(int(input())):
    x,y = [int(x) for x in input().split(" ")]
    if y == 0:
        print("divisao impossivel")
    else:
        valorfinal = x/y
        print(f"{valorfinal:.1f}")