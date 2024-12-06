valores = [int(x) for x in input().split(" ")]
a = valores[0]
valores.pop(0)
valores.sort(reverse = True)
b = valores[0]
y = 0

valorfinal = 0
while y >= 0 and y <= b-1:
    valorfinal += a + y
    y += 1
    
print(valorfinal)