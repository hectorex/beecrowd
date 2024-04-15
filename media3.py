splitas = input().split(" ")

a,b,c,d = map(float, splitas)


a = a*2
b = b*3
c = c*4
d = d*1

media = (a+b+c+d)/10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.")

elif media >= 5.0 and media <= 6.9:
    print("Aluno em exame.")
    e = float(input())
    print(f"Nota do exame: {e:.1f}")
    media = (media+e)/2
    if media >= 5.0:
        print("Aluno aprovado.")
        
    elif media <= 4.9:
        print("Aluno reprovado.")
    print(f"Media final: {media:.1f}")
