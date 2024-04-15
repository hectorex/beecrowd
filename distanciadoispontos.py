from math import sqrt

val1 = input()
val2 = input()

x1, y1 = val1.split(" ")
x2, y2 = val2.split(" ")

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)


distancia = sqrt((x2-x1)**2 + (y2-y1)**2)

print(f"{distancia:.4f}")

#usando o limitador de casas decimais com format f