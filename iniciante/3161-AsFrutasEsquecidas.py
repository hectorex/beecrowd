n,m = map(int, input().split())
frutas = []
lines = []
eat = []
for c in range(n):
    frutas.append(input().lower())

for c in range(m):
    lines.append(input().lower())

for i, fruta in enumerate(frutas):
    for y, line in enumerate(lines):
        if fruta in line or fruta[::-1] in line:
            eat.append(fruta)
            break

for fruta in frutas:
    if fruta in eat:
        print("Sheldon come a fruta", fruta)
    else:
        print("Sheldon detesta a fruta", fruta)