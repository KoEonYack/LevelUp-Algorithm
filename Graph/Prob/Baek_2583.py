"""
    @ 2583. 영역 구하기
    @ Prob. https://www.acmicpc.net/problem/2583
     Ref.
    @ Algo: DFS, BFS
    @ Start day: 19. 12. 26.
    @ End day: 19. 12.
"""


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def DFS(y, x):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny <= M and visited[ny][nx] is False and MAP[ny][nx] > 0:
            DFS(y, x)


def solution():
    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] is False and MAP[i][j] > 0:
                DFS(i, j)
                cnt += 1



# 가로 세로
N, M, BoxSize = map(int, input().split())
MAP = [[1] * N for _ in range(M)]
visited = [[False] * 100 for _ in range(100)]

for _ in range(BoxSize):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            MAP[i][j] = 0




"""
5 7 1
0 2 4 4
1 1 2 5
4 0 6 2

> 3
> 1 7 13
"""