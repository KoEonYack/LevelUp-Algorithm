"""
    @ 2225. 합분배
    @ Prob. https://www.acmicpc.net/problem/2225
     Ref.
    @ Algo: DP
    @ Start day: 20. 02. 17.
    @ End day: 20. 02. 17.
"""

N, K = map(int, input().split())

MAX_SIZE = 201
mod = 1000000000

DP = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]


for i in range(1, MAX_SIZE):
    DP[i][1] = DP[0][i] = 1

#for a in DP:
#    print(a)

for n in range(1, MAX_SIZE): # N 값
    for k in range(2, MAX_SIZE): # K 값
        for i in range(0, n+1):
            DP[n][k] = (DP[n][k] + DP[i][k-1]) % mod

#for a in DP:
#    print(a)

print(DP[N][K])

"""
1000000000
>

20 2
>
21
"""