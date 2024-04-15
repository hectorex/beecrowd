from math import sqrt


splitas = input().split(" ")

a, b, c = map(float, splitas)

delta = b**2-4*a*c

if delta < 0:
    print("Impossivel calcular")

elif delta == 0:
        delta = sqrt(delta)
        x1 = (-b + delta)/(2*a)
        print(f"R1 = {x1:.5f}\nR2 = {x1:.5f}")

elif delta > 0 and a != 0:
        delta = sqrt(delta)
        x1 = (-b + delta)/(2*a)
        x2 = (-b - delta)/(2*a)
        print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")

elif a == 0:
       print("Impossivel calcular")









