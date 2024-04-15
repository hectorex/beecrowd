splitas = input().split(" ")
x, y = map (float, splitas)

if x > 0.0 and y > 0.0:
            print("Q1")
    
elif x > 0.0 and y < 0.0:
            print("Q4")

elif x < 0.0 and y > 0.0:
            print("Q2")

elif x < 0.0 and y < 0.0:
            print("Q3")

elif x == 0 and y == 0:
            print("Origem")

elif x == 0 and y > 0.0 or x == 0 and y < 0.0:
        print("Eixo Y")

elif y == 0 and x > 0.0 or y == 0 and x < 0:
        print("Eixo X")



#TUDO DAQUI PRA BAIXO É SO PINADA

































# splitas = input("").split(" ")
# x, y = map (float, splitas)


# if (x == 0.0 and y == 0.0):
#     # no ponto 0
#     print("Origem")

# elif (x >= 0.01 and y >= 0.01) or (x >= 0.01 and y == 0.0) or (x == 0.00 and y >= 0.01):
#     # se x >= a 0.01 e y >= 0.01 É Q1

#     print("Q1")

# elif (x >= 0.01 and y <= -0.01) or (x == 0.00 and y <= -0.01) or (x >= 0.01 and y <= 0.00):
#     # se x >= 0.01 e y <= -0.01 é Q4

#     print("Q4")

# elif (x <= -0.01 and y >= 0.01) or (x <= 0.0 and y >= 0.01) or (x <= -0.01 and y == 0.0): 
#     # se x <= -0.01 e y >= 0.01

#     print("Q2")

# elif (x <= -0.01 and y <= -0.01) or (x == 0.0 and y <= -0.01) or (x <= -0.01 and y == 0.0): 
# #or x <= 0.0 and y <= -0.01 or x <= -0.01 and y <= 0.0:

#     print("Q3")









