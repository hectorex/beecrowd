vet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

string = input()

# Conversão de base 26 — igual converter "123" pra inteiro na base 10
# Cada letra é um "dígito": A=1, B=2, ..., Z=26
# Fórmula: total = total * 26 + digito_atual
#
# Exemplo com "AB":
#   i=0, c='A' → total = 0 * 26 + 1  = 1
#   i=1, c='B' → total = 1 * 26 + 2  = 28
#
# Exemplo com "ZZZ":
#   i=0, c='Z' → total = 0  * 26 + 26 = 26
#   i=1, c='Z' → total = 26 * 26 + 26 = 702
#   i=2, c='Z' → total = 702 * 26 + 26 = 18278 → não existe
total = 0
for c in string:
    total = total * 26 + (vet.index(c) + 1)  # vet.index(c)+1 converte letra → número

if total > 16384:  # XFD = 16384 é a última coluna do Excel
    print("Essa coluna nao existe Tobias!")
else:
    print(total)