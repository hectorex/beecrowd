numerodeconsultas = int(input())

while numerodeconsultas != 0:
    n,m = pontodivisor = input().split(" ")
    for c in range(numerodeconsultas):
        n = int(n)
        m = int(m)
        x,y = pontodecomparacao = input().split(" ")

        x = int(x)
        y = int(y)
        if x == n or y == m: print("divisa")
        elif x > n and y > m: print("NE")
        elif x > n and y < m: print("SE")
        elif x < n and y < m: print("SO")
        elif x < n and y > m: print("NO")
    numerodeconsultas = int(input())

