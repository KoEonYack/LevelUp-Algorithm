"""
    @ 1149. RGB거리
    @ Prob. https://www.acmicpc.net/problem/1149
     Ref.
    @ Algo: Recursion
    @ Start day: 20. 01. 12.
    @ End day: 20. 01. 12.
"""


N = int(input()) # 1000
A = [[0, 0, 0]]
D = [[0, 0, 0] for _ in range(N+1)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for i in range(1, N+1):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + A[i][0]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + A[i][1]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + A[i][2]

print(min(min(D[N][0], D[N][1]), D[N][2]))


"""
3
26 40 83
49 60 57
13 89 99  
>
96
"""