"""
    @ 2133. 타일 채우기
    @ Prob. https://www.acmicpc.net/problem/2133
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 21.
    @ End day: 20. 02. 21.
"""

N = int(input())
DP = [0] * (N+1)

DP[0] = 1
for i in range(N+1):
    if i % 2 == 0:
        DP[i] = DP[i-2]


"""
2
>
3
"""