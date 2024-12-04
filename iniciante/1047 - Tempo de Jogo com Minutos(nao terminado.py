#fazeeeeeeeeeeeer

split = input().split(" ")

a_h_inicial, b_m_inicial, c_h_final, d_m_final = map(int, split)

hora = 0
minuto = 0

def minuts():
    global hora
    if b_m_inicial == d_m_final:
        #aqui zerou
        hora += 1

    elif b_m_inicial < d_m_final:
        minuto = d_m_final - b_m_inicial
        #aqui vai faltar

    elif b_m_inicial > d_m_final:
        minuto = b_m_inicial - d_m_final
        minuto = 60 - minuto

def horas():
    global hora
    if a_h_inicial == c_h_final:
        #aqui zerou
        hora += 24

    elif a_h_inicial < c_h_final:
        hora += c_h_final - a_h_inicial
        #aqui vai faltar

    elif a_h_inicial > c_h_final:
        hora = a_h_inicial - c_h_final

minuts()
horas()

if hora == -1:
    hora = 0

print(f"{hora},{minuto}")
