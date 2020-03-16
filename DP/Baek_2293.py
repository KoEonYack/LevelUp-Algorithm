"""
    @ 2293. 동전
    @ Prob. https://www.acmicpc.net/problem/2293
     Ref.
    @ Algo: DP
    @ Start day: 20. 03. 10.
    @ End day: 20. 03. 10.
"""

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
DP = [0] * (N+1) # 10001

for i in range(N + 1):
    for j in range(len(coins)):
        if i >= coins[j]:
            if DP[i] > DP[i-coins[j]] + 1:
                DP[i] = DP[i-coins[j]] + 1

print(DP)


"""
3 10
1
2
5
>
10
"""