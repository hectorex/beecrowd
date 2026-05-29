p, n = map(int, input().split())

vet = [int(x) for x in input().split()]

rst = "YOU WIN"
for i in range (len(vet)-1):
    if vet[i] < vet[i+1] and vet[i]-vet[i+1] > p:
        rst = "GAME OVER"
    if abs(vet[i+1]-vet[i]) > p:
        rst = "GAME OVER"
print(rst)