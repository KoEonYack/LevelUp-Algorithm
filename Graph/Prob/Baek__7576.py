"""
    @ 7576. 토마토
    @ Prob. https://www.acmicpc.net/problem/7576
     Ref.
    @ Algo: BFS
    @ Start day: 20. 02. 15.
    @ End day: 20. 02. 15.
"""

from collections import deque

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# M 가로 크기, N 세로 크기
M, N = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
q = deque()
dist = [[-1]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == 0 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1


ans = max([max(row) for row in dist])
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 0 and dist[i][j] == -1:
            ans = -1


print(ans)


"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
>
8
---------------------
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
>-1
---------------------

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
>
6


"""

