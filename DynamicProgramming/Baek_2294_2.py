"""
    @ 2294. 동전 2
    @ Prob. https://www.acmicpc.net/problem/2294
     Ref.
    @ Algo: Recursion
    @ Start day: 20. 01. 31.
    @ End day: 20. 01. 31.
"""

import sys

def minCoins(N, S):
    if S == 0:
        return 0

    result = sys.maxsize
    for i in range(0, N):
        if coin[i] <= S:
            tmp = minCoins(N, S-coin[i])
            if tmp + 1 < result:
                result = tmp + 1

    return result


# K원 지불
N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
print(minCoins(len(coin), K))



"""
3 15
1
5
12
>
3


"""