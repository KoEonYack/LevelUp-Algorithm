Case = int(input())

for _ in range(Case):
    inputStr = list(input())
    openParn = 0

    for str in inputStr:
        if openParn < 0:
            print("No")
            break
        elif str is "(":
            openParn += 1
        elif str is ")":
            openParn -= 1

    if openParn is 0:
        print("Yes")
    else:
        print("No")