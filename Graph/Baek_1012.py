"""
    @ 1012. 유기농 배추
    @ Prob. https://www.acmicpc.net/problem/1012
     Ref.
    @ Algo: DFS, BFS
    @ Start day: 19. 12. 26.
    @ End day: 19. 12. 26.
"""


import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def DFS(y, x):
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < Y and 0 <= nx < X:
            if visited[ny][nx] is False and arr[ny][nx] > 0:
                DFS(ny, nx)


def solution():
    cnt = 0
    for y in range(Y):
        for x in range(X):
            if visited[y][x] is False and arr[y][x] > 0:
                DFS(y, x)
                cnt += 1

    print(cnt)


TestCase = int(input())
for _ in range(TestCase):
    X, Y, N = map(int, input().split())
    arr = [[0] * X for _ in range(Y)]
    visited = [[False] * X for _ in range(Y)]
    for i in range(N):
        x, y = map(int, input().split())
        arr[y][x] = 1

    solution()




"""


> 5
> 1
"""