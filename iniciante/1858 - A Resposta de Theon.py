n = int(input())

vet = [int(x) for x in input().split()]

minor = 21
min_index = 0
for index, num in enumerate(vet):
    if num < minor:
        minor = num
        min_index = index

print(min_index+1)
