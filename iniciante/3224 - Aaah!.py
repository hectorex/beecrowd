jon = str(input())
med = str(input())

if med == "h":
    rsp = "go"
elif len(med) > len(jon):
    rsp = "no"
elif len(med) < len(jon):
    rsp = "go"
elif len(med) == len(jon):
    rsp = "go"

print(rsp)