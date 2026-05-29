tday = 2015
for c in range(int(input())):
    year = int(input())
    if year > tday:
        print(f"{abs(year-tday)+1} A.C.")
    elif year == tday:
        print(f"{abs(year-tday)+1} A.C.")
    else:
        print(f"{abs(year-tday)} D.C.")