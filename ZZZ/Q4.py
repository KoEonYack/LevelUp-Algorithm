

def moves(a):
    ans = 0
    numOfEven = 0

    for i in range(len(a)):
        if a[i] % 2 == 0:
            numOfEven += 1

    for i in range(numOfEven):
        if a[i] % 2 != 0:
           ans += 1

    return ans


print(moves([1]))
print(moves([6, 3, 4, 5]))
print(moves([13, 10, 21, 20]))
print(moves([8, 5, 11, 4, 6]))
