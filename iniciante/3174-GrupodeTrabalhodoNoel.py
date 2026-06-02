p = 0

p_b = 0
p_a = 0
p_m = 0
p_d = 0

for c in range(int(input())):
    e, g, h = (str(x) for x in str(input()).split())
    h = int(h)
    if (g=="bonecos"):
        p_b += h
    elif (g=="arquitetos"):
        p_a += h
    elif (g=="musicos"):
        p_m += h
    elif (g=="desenhistas"):
        p_d += h

p = (p_b//8)+(p_a//4)+(p_m//6)+(p_d//12)
    
print(p)