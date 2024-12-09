c,n = [int(x) for x in input().split()]
variavel = n
while c > n:
    c -= n
while c < n:
    c = c
    break
if c == variavel:
    c -= variavel
print(c)
    
