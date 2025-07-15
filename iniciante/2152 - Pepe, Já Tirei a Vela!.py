for c in range(int(input())):
    hour,minute,op_cl = (int(x) for x in input().split())
    if op_cl == 1: op_cl = "abriu"
    if op_cl == 0: op_cl = "fechou"
    if int(hour) < 10: hour = "0"+str(hour)
    if int(minute) < 10: minute = "0"+str(minute)
    print(f"{hour}:{minute} - A porta {op_cl}!")
