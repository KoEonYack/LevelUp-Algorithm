"""
    @ 2294. 동전 2
    @ Prob. https://www.acmicpc.net/problem/2294
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 20.
    @ End day: 20. 01. 20.
"""

import sys

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
dy = [10001] * (K+1)
dy[0] = 0
for i in range(N):
    for j in range(coin[i], K+1):
        dy[j] = min(dy[j], dy[j-coin[i]]+1)

dy[-1] = dy[-1] if dy[-1] != 10001 else -1
print(dy[-1])



"""
3 15
1
5
12
>
3
"""