"""
    @ 2156. 포도주 시식
    @ Prob. https://www.acmicpc.net/problem/2156
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""


N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
DP = [0] * (N+1)

DP[1] = arr[1]
if N >= 2:
    DP[2] = arr[1] + arr[2]

for i in range(3, N+1):
    DP[i] = DP[i-1]              # 현재 포도주 마시지 않음
    if DP[i] < DP[i-2] + arr[i]: # 2칸 전, 현재 포도주 마심
        DP[i] = DP[i-2] + arr[i]
    if DP[i] < DP[i-3] + arr[i] + arr[i-1]: # 3칸 전, 현재, 이전포도주 마심
        DP[i] = DP[i-3] + arr[i] + arr[i-1]


print(DP[N])

"""
6
6
10
13
9
8
1
>
33
"""