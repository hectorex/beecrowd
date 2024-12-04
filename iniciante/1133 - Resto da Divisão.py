x = int(input())
y = int(input())
if x > y:
    a = x
    b = y
else:
    a = y
    b = x

for c in range(b,a):
    if c%5 == 2 and c != -2 and c != 2 or c%5 == 3 and c != -2 and c!= 2:
        print(c)
