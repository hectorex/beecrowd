i = 1
j = 7
for y in range(5):
    j = 7
    for c in range(3):
        print(f"I={i} J={j}")
        j -= 1
    if y == 0:
        i = 3
    else:
        i = i+2




