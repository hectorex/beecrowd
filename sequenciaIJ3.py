i = 1
j = 0

for c in range(5):
    j = i+6
    for c in range(3):
        print(f"I={i} J={j}")
        j -= 1
    i += 2

