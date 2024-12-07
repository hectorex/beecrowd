nota = int(input())
if nota == 0:
    rsp = "E"
elif nota >= 1 and nota <= 35:
    rsp = "D"
elif nota >= 36 and nota <= 60:
    rsp = "C"
elif nota >= 61 and nota <= 85:
    rsp = "B"
elif nota >= 86 and nota <= 100:
    rsp = "A"
print(rsp)