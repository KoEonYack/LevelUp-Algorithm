'''
    87. 섬나라 아일렌드 (DFS)
    @ TestCase:
7 7
1 1 0 0 0 1 0
0 1 1 0 1 1 0
0 1 0 0 0 0 0
0 0 0 1 0 1 1
1 1 0 1 1 0 0
1 0 0 0 1 0 0
1 0 1 0 1 0 0

    Ref. https://www.acmicpc.net/problem/14716
    @ Start day: 19. 11. 30.
    @ End day: 19. 11. 30.
'''

import sys
sys.setrecursionlimit(100000)


Y, X = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(Y)]
check = [[False] * X for _ in range(Y)]
ans = 0


def dfs(x, y):
    check[x][y] = True
    for dx, dy in (-1,0), (1,0), (-1,1), (0,1), (1,1), (-1,-1), (0,-1), (1,-1):
        nx, ny = x+dx, y+dy
        if nx < 0 or nx >= Y or ny < 0 or ny >= X:
            continue
        if check[nx][ny] is False and MAP[nx][ny] == 1:
            dfs(nx, ny)


for i in range(Y):
    for j in range(X):
        if check[i][j] is False and MAP[i][j] == 1:
            dfs(i, j)
            ans += 1

print(ans)
