n = int(input())
for c in range(n):
    vet = [int(x) for x in input().split()]
    total = sum(vet)-vet[0]-(len(vet)-2)
    print(total)