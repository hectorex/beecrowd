splitas = input().split(" ")
a,b,c = map(int, splitas)

a1 = a
a2 = b
a3 = c

deucerto = False

if a < b and a < c:
    deucerto = True
    print(a)
    if b < c:
        print(b)
        print(c)
    else:
        print(c)
        print(b)
elif b < a and b < c and deucerto == False:
    deucerto == True
    print(b)
    if a < c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
elif c < a and c < b and deucerto == False:
    print(c)
    if a < b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)

print("")
print(a1)
print(a2)
print(a3)