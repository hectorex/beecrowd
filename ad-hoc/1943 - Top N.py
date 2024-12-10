a = int(input())
if a == 1:
    top = 1
elif a <= 3:
    top = 3
elif a <= 5:
    top = 5
elif a <= 10:
    top = 10
elif a <= 25:
    top = 25
elif a <= 50:
    top = 50
elif a <= 100:
    top = 100

print(f"Top {top}")