"""
    @ Baek 17086. 아기 상어2
    @ Prob. https://www.acmicpc.net/problem/17086
     Ref.
    @ Algo: BFS
    @ Start day: 20. 09. 23.
    @ End day: 20. 09. 23.
"""

from collections import deque

# N:세로, M: 가로 5, 4
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
check = [[-1] * M for _ in range(N)]
dx = (-1, -1, -1, 0, 1, 1, 1, 0)
dy = (-1, 0, 1, 1, 1, 0, -1, -1)

q = deque()
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            q.append((i, j))
            check[i][j] = 0

ans = 0
while q:
    x, y = q.popleft()
    for i in range(8):
        nx = x + dx[i]; ny = y + dy[i] 
        if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == -1:
            check[nx][ny] = check[x][y] + 1
            ans = max(ans, check[nx][ny])
            q.append((nx, ny))

print(ans)


"""
5 4
0 0 1 0
0 0 0 0
0 0 0 1
1 0 0 0
0 0 0 0
>
2
-----------------
7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
>
2
"""

