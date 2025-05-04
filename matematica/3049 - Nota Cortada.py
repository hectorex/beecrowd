a = int(input())
b = int(input())
retangulo = 160*70
trapezio = ((a+b)*70)/2
if trapezio == retangulo/2:
    rslt = 0
elif trapezio > retangulo/2:
    rslt = 1
else:
    rslt = 2
print(rslt)