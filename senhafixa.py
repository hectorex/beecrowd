senha_correta = 2002

x = int(input())

while x != senha_correta:
    print("Senha Invalida")
    x = int(input())
print("Acesso Permitido")