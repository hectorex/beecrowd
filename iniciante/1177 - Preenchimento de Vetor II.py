t = int(input())
n = 0
while n < 1000:
    for i in range(0,t):
        print(f"N[{n}] = {i}")
        n += 1
        if n >= 1000:
            exit()