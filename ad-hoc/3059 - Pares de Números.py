nms,mini,max = [int(x) for x in input().split()]
nms = [int(y) for y in input().split()]
val1 = 0
pares = 0
for c in range(len(nms)-1):
    for item in nms:
        if item != nms[val1]:
            if item+nms[val1] >= mini and item+nms[val1] <= max:
                pares += 1
        else:
            pass
    nms.remove(nms[val1])
print(pares)
