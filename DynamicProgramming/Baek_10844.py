"""
    @ 10844. 쉬운 계단 수
    @ Prob. https://www.acmicpc.net/problem/10844
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 14.
    @ End day: 20. 02. 14.
"""


N = int(input())
mod = 1000000000
DP = [[0] * (N+1) for _ in range(10)]

for i in range(1, 10):
    DP[i][1] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        if j == 0:
            DP[0][i] = DP[1][i-1]
        elif j == 9:
            DP[9][i] = DP[8][i-1]
        else:
            DP[j][i] = (DP[j-1][i-1] + DP[j+1][i-1]) % mod

#for a in DP:
#    print(a)

total_V = 0
for i in range(10):
    total_V = (total_V + DP[i][N]) % mod

print(total_V)

"""
1
>
9
-----------------
2
>
17
"""