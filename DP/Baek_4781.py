"""
    @ Baek 4781. 사탕 가게
    @ Prob. https://www.acmicpc.net/problem/4781
     Ref.
    @ Algo: DP(0-1 Knapsack)
    @ Start day: 20. 04. 06.
    @ End day: 20. 04. 06.
"""

def maxCalorie(cash):
    cash = int(cash)
    print("test", cash)
    result = cache[cash]
    if result != -1:
        return result

    result = 0
    for i in range(N):
        if cash - candy[i][1] >= 0:
            result = max(result, candy[i][0] + maxCalorie(cash - candy[i][1]))
    return result


cache = [-1] * (100 * 100 + 1)
candy = [0] * (5000 + 1)

while True:
    N, M = map(str, input().split())
    if int(N) == 0 and M == "0.00":
        break
    N = int(N)
    for i in range(N):
        C, P = map(float, input().split())
        candy[i] = [C, (P*100 + 0.5)]
    print(maxCalorie(int(float(M) * 100 + 0.5)))


"""
2 8.00
700 7.00
199 2.00
3 8.00
700 7.00
299 3.00
499 5.00
0 0.00
>
796
798

"""



