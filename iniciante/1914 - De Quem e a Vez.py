a = int(input())

for i in range(a):
    player1, choice1, player2, choice2 = map(str, input().split(" "))
    num1, num2 = map(int, input().split(" "))
    if (num1+num2)%2 == 0:
        if (choice1 == "PAR"):
            print(player1)

        else:
            print(player2)
    elif (choice2 == "IMPAR"):
        print(player2)
    else:
        print(player1)