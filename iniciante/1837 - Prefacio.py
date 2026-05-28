a, b = map(int, input().split())

rest = a%abs(b)

print(f"{(a-rest)//b} {rest}")