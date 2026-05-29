rsp = "Minimum note not reached"

highnote = float('-inf')
for c in range(int(input())):
    id,note = map(float, input().split())
    id = int(id)
    if note > highnote and note >= 8:
        highnote = note
        rsp = id


print(rsp)
