"""
    @ Baek 2482 색상환
    @ Prob. https://www.acmicpc.net/problem/2482
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 30.
    @ End day: 20. 03. 30.
"""

mod = 1000000003
N = int(input())
K = int(input())

DP = [[0] * 1001 for _ in range(1001)]

for i in range(N+1):
    DP[i][1] = i
    DP[i][0] = 1


for i in range(2, N+1):
    for j in range(2, K+1):
        DP[i][j] = (DP[i-2][j-1] + DP[i-1][j]) % mod

print((DP[N-1][K] + DP[N-3][K-1]) % mod)


"""
4
2
>
2
"""

