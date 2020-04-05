"""
    @ Baek 16948. 데스 나이트
    @ Prob. https://www.acmicpc.net/problem/16948
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

N = int(input())
check = [[-1]*N for i in range(N)]
r1, c1, r2, c2 = map(int, input().split())
dx = (-2, -2, 0, 0, 2, 2)
dy = (-1, 1, -2, 2, -1, 1)

q = deque()
q.append((r1, c1))
check[r1][c1] = 0

while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == -1:
            check[nx][ny] = check[x][y] + 1
            q.append((nx, ny))

# for a in check:
#     print(a)

print(check[r2][c2])


"""
7
6 6 0 1
>
4
---------------
6
5 1 0 5
>
-1
---------------
7
0 3 4 3
>
2
"""


