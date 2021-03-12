"""
    @ Baek 11567. 선진이의 겨울 왕국
    @ Prob. https://www.acmicpc.net/problem/11567
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# M: 세로 N: 가로
M, N = map(int, input().split())
MAP = [list(input()) for _ in range(M)]
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())
q = deque()
q.append((sx-1, sy-1))
t = [0, 0]

if MAP[ex-1][ey-1] == 'X':
    print("NO")
else:
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if nx == ex - 1 and ny == ny - 1:
                    break
                elif MAP[nx][ny] != 'X':
                    q.append((nx, ny))
                    MAP[nx][ny] = "X"
                    print(nx, ny)

for a in MAP:
    print(a)




"""
4 6
X...XX
...XX.
.X..X.
......
1 6
2 2
>
YES
--------------
5 4
.X..
...X
X.X.
....
.XX.
5 3
1 1
>
NO
----------------
4 7
..X.XX.
.XX..X.
X...X..
X......
2 2 
1 6
>
YES

"""