val1 = input()
vet = []
while val1 != "</html>":
    val1 = input()
    if val1 == "    <body>":
        while val1 != "    </body>":
            val1 = input()
            if val1 != "    </body>":
                vet.append(val1)
                

for string in vet:
    print(string)

