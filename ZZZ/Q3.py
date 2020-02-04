
def minX(arr):
    ans = 0
    culSum = 0
    minV = 0
    for i in range(len(arr)):
        culSum += arr[i]
        if culSum < 1 and minV > culSum:
            minV = culSum

    return abs(minV)+1


print(minX([-2, 3, 1, -5]))
print(minX([-5, 4, -2, 3, 1, -1, -6, -1, 0, -5]))
print(minX([-1, -1, 0]))





