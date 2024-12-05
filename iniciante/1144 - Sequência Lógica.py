n = int(input())
a = 1
print(a,a,a)
print(a,a+1,a+1)
for c in range(n-1):
    a += 1
    print(a,a**2,(a**2)*a)
    print(a,(a**2)+1,((a**2)*a)+1)