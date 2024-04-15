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

if e >= f+g:
    print("NAO FORMA TRIANGULO")

elif e**2 == (f**2 + g**2):
    print("TRIANGULO RETANGULO")

elif e**2 > (f**2 + g**2):
    print("TRIANGULO OBTUSANGULO")

elif e**2 < (f**2 + g**2):
    print("TRIANGULO ACUTANGULO")



if e == f and e == g:
    print("TRIANGULO EQUILATERO")

elif e == f and e != g or f == g and f != e or g == e and g != f:
    print("TRIANGULO ISOSCELES")
