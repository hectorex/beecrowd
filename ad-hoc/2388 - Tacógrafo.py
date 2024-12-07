n = int(input())
total = 0
for c in range(n):
    a,b = [int(x) for (x) in input().split()]
    total += a*b

print(total)