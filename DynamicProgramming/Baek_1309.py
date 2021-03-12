"""
    @ 1309. 동물원
    @ Prob. https://www.acmicpc.net/problem/1309
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 19.
    @ End day: 20. 02. 19.
"""

N = int(input())
DP = [[0] * 3 for _ in range(N+1)]
mod = 9901
DP[0][0] = 1
for i in range(1, N+1):
    DP[i][0] = (DP[i-1][0] + DP[i-1][1] + DP[i-1][2]) % mod
    DP[i][1] = (DP[i-1][0] + DP[i-1][2]) % mod
    DP[i][2] = (DP[i-1][0] + DP[i-1][1]) % mod

print(sum(DP[i]) % mod)

"""
4
>
41
"""
