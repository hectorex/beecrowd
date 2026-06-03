pib = 100.0

a,b = map(float, input().split())

rst = (1 + a/100) * (1 + b/100) * 100 - 100

print(f"{rst:.6f}")
