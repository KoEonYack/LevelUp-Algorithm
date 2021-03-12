"""
    @ 1261. 알고스팟
    @ Prob. https://www.acmicpc.net/problem/1261
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 13.
    @ End day: 20. 03. 13.
"""

from collections import deque

# 가로, 세로
M, N = map(int, input().split())
MAP = [list(map(int, [*input()])) for _ in range(N)]
D = [[-1]*(M+1) for _ in range(N+1)]
q = deque()
D[0][0] = 0
q.append((0, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and D[nx][ny] == -1:
            if MAP[nx][ny] == 0:
                D[nx][ny] = D[x][y]
                q.appendleft((nx, ny))
            else:
                D[nx][ny] = D[x][y] + 1
                q.append((nx, ny))

print(D[N-1][M-1])

#for a in MAP:
#    print(a)

"""
3 3
011
111
110
>
3
-----------
6 6
001111
010000
001111
110001
011010
100010
>
2
"""