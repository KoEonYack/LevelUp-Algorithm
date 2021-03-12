"""
    @ 11048. 이동하기
    @ Prob. https://www.acmicpc.net/problem/11048
      Ref.
    @ Algo: DP
    @ Start day: 20. 02. 25.
    @ End day: 20. 02. 25.
"""

# N: 세로, M: 가로
N, M = map(int, input().split())
A = [[0] * M]
DP = [[0] * (M+1) for _ in range(N+1)]

for _ in range(N):
    A.append([0] + list(map(int, input().split())))

for i in range(1, N+1):
    DP[i][1] = DP[i-1][1] + A[i][1]
for i in range(1, M+1):
    DP[1][i] = DP[1][i-1] + A[1][i]

for i in range(2, N+1):
    for j in range(2, M+1):
        DP[i][j] = max(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + A[i][j]

#for a in DP:
#    print(a)

print(DP[-1][-1])


"""
3 4
1 2 3 4
0 0 0 5
9 8 7 6
>
31

"""

