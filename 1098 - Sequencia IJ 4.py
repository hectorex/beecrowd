i = 0
j = 1

for c in range(11):
    j = i
    for y in range(3):
        if c == 10:
            j += 1 
            i = int(f"{i:.0f}")
            j = int(f"{j:.0f}")
            print(f"I={i} J={j}")

        elif i != 0.0 and i != 1.0:
            j += 1
            print(f"I={i:.1f} J={j:.1f}")


        else:
            j += 1
            print(f"I={i:.0f} J={j:.0f}") 


    i += 0.20


