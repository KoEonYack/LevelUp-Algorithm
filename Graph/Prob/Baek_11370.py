"""
    @ Baek 11370. Spawn of Ungoliant
    @ Prob. https://www.acmicpc.net/problem/11370
     Ref.
    @ Algo: BFS
    @ Start day: 20. 04. 10.
    @ End day: 20. 04. 10.
"""

def BFS():

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy; nx = x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if ch[ny][nx] == 0 and MAP[ny][nx] == "T":
                    q.append((ny, nx))
                    ch[ny][nx] = 1
                    MAP[ny][nx] = 'S'


from collections import deque

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: break
    MAP = [list(input()) for _ in range(H)]
    ch = [[0]*W for _ in range(H)]

    q = deque()
    for i in range(H):
        for j in range(W):
            if MAP[i][j] == "S":
                ch[i][j] = 1
                q.append((i, j))
                BFS()

    for a in MAP:
        print("".join(a))


"""
3 4
T..
TST
..T
TTT

5 5
T.T.T
.T.T.
..S..
.T.T.
T.T.T
0 0
>
S..
SSS
..S
SSS
T.T.T
.T.T.
..S..
.T.T.
T.T.T
"""