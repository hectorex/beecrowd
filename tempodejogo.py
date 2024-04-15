# primeirodei = str(input()).split(" ")
# informacoesdei1 = str(input()).split(" : ")

# segundodei = str(input()).split(" ")
# informacoesdei2 = str(input()).split(" : ")

# dletras, numerododia = map(str, primeirodei)

# numerododia = int(numerododia)

# dletras2, numerododia2 = map(str, segundodei)

# numerododia2 = int(numerododia2)

# horas1, minutos1, segundos1 = map(int, informacoesdei1)

# horas2, minutos2, segundos2 = map(int, informacoesdei2)


# dias = abs(numerododia - numerododia2)
# horas = abs(24 -(horas1 - horas2))
# minutos = abs(minutos1 - minutos2)
# segundos = abs(segundos1 - segundos2)


# print(horas,minutos,segundos, dias)



# if horas >= 25:
#     horas -= 24
#     if numerododia != numerododia2 and dias == 1:
#         dias = dias

# elif horas == 24 and dias == 1:
#     horas = 0
#     dias = 1

# elif horas == 24 and dias != 1:
#     horas = 0
#     dias += 1

# elif horas1 > horas2:
#     dias -= 1
# elif horas1 == horas2:
#     dias = dias
#     if minutos1 > minutos2:
#         dias -=1
#     elif minutos1 == minutos2:
#         dias = dias
#         if segundos1 > segundos2:
#             dias -= 1




# print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
               

primeirodei = str(input()).split(" ")
informacoesdei1 = str(input()).split(" : ")

segundodei = str(input()).split(" ")
informacoesdei2 = str(input()).split(" : ")

dletras, numerododia = map(str, primeirodei)

numerododia = int(numerododia)

dletras2, numerododia2 = map(str, segundodei)

numerododia2 = int(numerododia2)

horas1, minutos1, segundos1 = map(int, informacoesdei1)

horas2, minutos2, segundos2 = map(int, informacoesdei2)


dias = abs(numerododia - numerododia2)
horas = abs(24 -(horas1 - horas2))
minutos = abs(minutos1 - minutos2)
segundos = abs(segundos1 - segundos2)

if horas1 > horas2:
    dias -= 1

elif horas == 24:
    horas = 0
    dias += 1

elif horas > 24:
    while horas >= 24:
        horas -= 24
        dias += 1

elif numerododia == numerododia2 and horas2 > horas1:
    dias += 1

elif horas1 == horas2:
    dias = dias
    if minutos1 > minutos2:
        dias -=1
    elif minutos1 == minutos2:
        dias = dias
        if segundos1 > segundos2:
            dias -= 1




print(f"{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)")
               







