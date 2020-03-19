"""
    @ Baek 16930. 달리기
    @ Prob. https://www.acmicpc.net/problem/16930
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# N:세로 M:가로, K: step
N, M, K = map(int, input().split())
D = [list(input()) for _ in range(N)]
sx, sy, ex, ey = map(int, input().split())
sx -= 1; sy -= 1; ex -= 1; ey -=1
check = [[float('inf')]*M for _ in range(N)]
q = deque()
q.append((sx, sy))
check[sx][sy] = 0

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        nk = 1
        while nk <= K and 0 <= nx < N and 0 <= ny < M and D[nx][ny] != '#' and check[nx][ny] > check[x][y]:
            if check[nx][ny] == float('inf'):
                q.append((nx, ny))
                check[nx][ny] = check[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1

# for a in check:
#     print(a)

if check[ex][ey] == float('inf'):
    print(-1)
else:
    print(check[ex][ey])



"""
3 4 4
....
###.
....
1 1 3 1
>
3
---------------
3 4 1
....
###.
....
1 1 3 1
>
8
---------------
2 2 1
.#
#.
1 1 2 2
>
-1
"""