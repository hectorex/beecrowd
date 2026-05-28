a, b = [int(x) for x in input().split()]

rest = a%abs(b)

print(f"{(a-rest)/b:.0f} {rest}")