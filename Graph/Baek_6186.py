"""
    @ Baek 6186. Best Grass
    @ Prob. https://www.acmicpc.net/problem/6186
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
            if 0 <= ny < N and 0 <= nx < M:
                if ch[ny][nx] == 0 and MAP[ny][nx] == '#':
                    q.append((ny, nx))
                    ch[ny][nx] = 1


from collections import deque


# 세로, 가로
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
ch = [[0] * M for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

q = deque()
res = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == "#" and ch[i][j] == 0:
            q.append((i, j))
            ch[i][j] = 1
            BFS()
            res += 1

print(res)

"""
5 6
.#....
..#...
..#..#
...##.
.#....
>
5

"""