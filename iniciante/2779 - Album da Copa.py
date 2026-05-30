album = int(input())
arr = []
for c in range(int(input())):
    num = int(input())
    if num not in arr:
        arr.append(num)
print(album-len(arr))