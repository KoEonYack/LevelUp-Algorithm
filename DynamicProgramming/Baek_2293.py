"""
    @ Baek 2293. 동전
    @ Prob. https://www.acmicpc.net/problem/2293
      Ref.  https://mong9data.tistory.com/68
    @ Algo: DP
    @ Start day: 20. 03. 10.
    @ End day: 20. 09. 05.
"""

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
DP = [0] * (K+1)
DP[0] = 1

for coin in coins:
    for j in range(coin, K+1):
        if j - coin >= 0:
            DP[j] = DP[j] + DP[j-coin]

print(DP[K])

"""
3 10
1
2
5
>
10
"""