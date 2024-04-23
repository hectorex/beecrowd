positivos = 0
somapositivos = 0

for c in range(6):
    a = float(input())
    if a > 0:
        positivos += 1
        somapositivos += a

print(f"{positivos} valores positivos")
media = somapositivos/positivos
print(f"{media:.1f}")