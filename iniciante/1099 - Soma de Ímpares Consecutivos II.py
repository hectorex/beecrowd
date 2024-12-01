x = int(input())

for c in range(x):
    soma = 0
    splitas = input().split(" ")
    x,y = map(int, splitas)
    if y > x:
        for c in range (x+1,y):
            if c%2 != 0:
                soma += c  
    else:
        for c in range (y+1,x):
            if c%2 != 0:
                soma += c
    print(soma)
