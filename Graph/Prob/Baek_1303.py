"""
    @ Baek 1303. 전쟁 - 전투
    @ Prob. https://www.acmicpc.net/problem/1303
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 18.
    @ End day: 20. 03. 18.
"""

from collections import deque

def BFS():
    q.append((i, j))
    check[i][j] = 1
    t = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and MAP[nx][ny] == MAP[x][y] and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))
                t += 1
    return t

# N: 가로 M : 세로
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
check = [[0] * N for _ in range(M)]

dx,dy=[1,-1,0,0],[0,0,1,-1]
q = deque()
B, W = 0, 0

for i in range(M):
    for j in range(N):
        if check[i][j] == 0:
            ans = BFS()
            if MAP[i][j] == 'W': W += ans ** 2
            else: B += ans ** 2

print(W, B)

"""
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
>
130 65
----------------------
5 3
WBWWW
WWWWW
WWWWW

"""
