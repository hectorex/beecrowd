num = input()
num = num[::-1]
if num[0] == "0":
    print(0, end="")
num = int(num)
print(num)