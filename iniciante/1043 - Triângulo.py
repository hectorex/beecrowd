splitas = input().split(" ")

a, b, c = map(float, splitas)

e = 0
f = 0
g = 0

passouja = False

if  a > b and a > c:
    passouja = True
    e = a
    if b > c:
        f = b
        g = c
    else:
        f = c
        g = b

elif b > a and b > c and passouja == False:
    e = b
    if a > c:
        f = a
        g = c
    else:
        f = c
        g = a

else:
    e = c
    if a > b:
        f = a
        g = b
    else:
        f = b
        g = a

perimetro = e+f+g

if e + f > g and g > e - f:
    print(f"Perimetro = {perimetro}")

elif f + g > e and e > f - g:
    print(f"Perimetro = {perimetro}")

elif g + e > f and f > e - g:
    print(f"Perimetro = {perimetro}")

else: 
    area = ((a+b)*c)/2
    print(f"Area = {area}")
