n = int(input())
a,b,c = [int(x) for x in input().split()]
if a >= n and b >= n and c >= n: rsp = "S"
else: rsp = "N"
print(rsp)