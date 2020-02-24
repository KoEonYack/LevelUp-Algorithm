"""
    @ 17404. RGB거리 2
    @ Prob. https://www.acmicpc.net/problem/17404
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 24.
    @ End day: 20. 02. 24.
"""


N = int(input()) # 1000
A = [[0, 0, 0]]
D = [[0, 0, 0] for _ in range(N+1)]

for _ in range(N):
    A.append(list(map(int, input().split())))


ans = 1000*1000 + 1

for k in range(2+1):
    for j in range(2+1):
        if j == k:
            D[1][j] = A[1][j]
        else:
            D[1][j] = 1000*1000 + 1

    for i in range(2, N+1):
        D[i][0] = min(D[i-1][1], D[i-1][2]) + A[i][0]
        D[i][1] = min(D[i-1][0], D[i-1][2]) + A[i][1]
        D[i][2] = min(D[i-1][0], D[i-1][1]) + A[i][2]

    for j in range(2+1):
        if j == k: continue
        ans = min(ans, D[N][j])

print(ans)

"""
3
26 40 83
49 60 57
13 89 99
>
110
"""