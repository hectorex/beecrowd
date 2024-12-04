print("MUITO OBRIGADO")
alcool = 0
gasosa = 0
diesel = 0
while True:
    x = int(input())
    if x == 1: alcool += 1
    elif x == 2: gasosa += 1
    elif x == 3: diesel += 1
    elif x == 4: break

print(f"Alcool: {alcool}\nGasolina: {gasosa}\nDiesel: {diesel}")