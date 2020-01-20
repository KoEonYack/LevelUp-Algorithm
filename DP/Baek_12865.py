"""
    @ 12865. 평범한 배낭
    @ Prob. https://www.acmicpc.net/problem/12865
     Ref.
    @ Algo: DP
    @ Start day: 20. 01. 20.
    @ End day: 20. 01. 20.
"""


N, K = map(int, input().split())
dy = [0] * (K+1)

bag = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(K, 1, -1):
        if bag[i][0] <= j:
            dy[j] = max(dy[j], dy[j-bag[i][0]]+bag[i][1])

print(dy[-1])

"""
4 11
5 12
3 8
6 14
4 8
>
28

W V
4 7
6 13
4 8
3 6
5 12
>   
14
"""
