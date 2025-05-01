for c in range(int(input())):
    nmr = int(input())
    primo = "eh primo"
    for i in range(2,nmr-1):
        if nmr%i == 0:
            primo = "nao eh primo"
    print(nmr,primo)