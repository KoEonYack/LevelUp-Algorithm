"""
    @ 16929. Two dots
    @ Prob. https://www.acmicpc.net/problem/16929
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 02. 16.
    @ End day: 20. 02. 16.
"""

import sys
sys.setrecursionlimit(100000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(x, y, cnt, color):
    if check[x][y]:
        if cnt - dist[x][y] >= 4:
            return True
        else:
            return False

    check[x][y] = True
    dist[x][y] = cnt

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if MAP[nx][ny] == color:
                if go(nx, ny, cnt+1, color):
                    return True

    return False


# M: 가로, N: 세로
N, M = map(int, input().split())
MAP = [input() for _ in range(N)]
check = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if check[i][j]:
            continue

        dist = [[0]*M for _ in range(N)]
        ok = go(i, j, 1, MAP[i][j])
        if ok:
            print("Yes")
            sys.exit()

print("No")

"""
3 4
AAAA
ABCA
AAAA
>
Yes
-------------
3 4
AAAA
ABCA
AADA
>
No
"""