#SOLUÇÃO DO GEPETOS

splitas = input().split(" ")

inicialH, inicialM, finalH, finalM = map(int, splitas)

def horasa():
    if inicialH > finalH:
        return 24 - abs(inicialH - finalH)
    else:
        return abs(finalH - inicialH)

def minutosa():
    if inicialM <= finalM:
        return finalM - inicialM
    else:
        return 60 - abs(inicialM - finalM)

horas = horasa()
minutos = minutosa()

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")

# AQUI DEU CERTO

splitas = input().split(" ")

inicialH, inicialM, finalH, finalM = map(int, splitas)

horas = 0
minutos = 0


def horasa():
    global horas
    if inicialH > finalH:
        horas = 24 - (inicialH - finalH)
    elif finalH > inicialH:
        horas = finalH - inicialH
    elif inicialH == finalH and finalM > inicialM:
        horas = 0
    elif inicialH == finalH and inicialM > finalM:
        horas = 24

def minutosa():
    global minutos 
    global horas

    if inicialM < finalM:
        minutos = finalM - inicialM    
    elif inicialM > finalM:
        horas -= 1
        minutos = 60 - (inicialM - finalM)

if inicialH == finalH and inicialM == finalM:
    horas = 24

horasa()
minutosa()

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")  # splitas = input().split(" ")

# inicialH, inicialM, finalH, finalM = map(int, splitas)

# horas = 0
# minutos = 0

# def calculohora():
#     global horas

#     if inicialH == finalH:
#         horas += 24

#     elif inicialH > finalH:
#         horas += 24 - inicialH - finalH

#     elif finalH > inicialH:
#         horas += finalH - inicialH  

# def calcularminuto():
#     global minutos
#     global horas

#     if inicialM == finalM:
#         horas += 1
#     elif inicialM > finalM:
#         horas -= 1
#         minutos = 59
#     elif finalM > inicialM:
#         minutos += finalM - inicialM



# calculohora()
# calcularminuto()

# if horas > 24:
#     horas = 24

# print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")




