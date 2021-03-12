"""
    @ Baek 2738 행렬 덧셈
    @ Prob. https://www.acmicpc.net/problem/2738
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

N, M = map(int, input().split())
A = []
B = []
for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        A[i][j] += B[i][j]

for a in A:
    print(*a)

"""
3 3
1 1 1
2 2 2
0 1 0
3 3 3
4 4 4
5 5 100
>
4 4 4
6 6 6
5 6 100

"""
