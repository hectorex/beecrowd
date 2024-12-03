while True:
    x,y = [int(x) for x in input().split(" ")]
    if x == y: break
    if x > y: print("Decrescente")
    else: print("Crescente")
