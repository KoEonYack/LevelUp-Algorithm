

import sys

N = int(sys.stdin.readline())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * (N+1) for _ in range(N+1)]

DP[0][0] = A[0][0]

#k=2
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            DP[i][j] = A[i][j] + DP[i-1][j]
        elif i == j:
            DP[i][j] = A[i][j] + DP[i-1][j-1]
        else:
            DP[i][j] = max(DP[i-1][j-1], DP[i-1][j]) + A[i][j]
    #k += 1

#for a in DP:
#    print(a)

print(max(DP[N-1]))

"""
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
>
30
"""