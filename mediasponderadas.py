n = int(input())

for c in range(n):
    splitas = input().split(" ")
    a, b, c = map(float, splitas)
    media = ((a*2)+(b*3)+(c*5))/10
    print(f"{media:.1f}")