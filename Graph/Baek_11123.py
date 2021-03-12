"""
    @ Baek 11123. 양 한마리... 양 두마리...
    @ Prob. https://www.acmicpc.net/problem/11123
     Ref.
    @ Algo: BFS
    @ Start day: 20. 04. 10.
    @ End day: 20. 04. 10.
"""

from collections import deque

def BFS():

    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy; nx = x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if ch[ny][nx] == 0 and MAP[ny][nx] == '#':
                    q.append((ny, nx))
                    ch[ny][nx] = 1


dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())     # 세로, 가로
q = deque()
MAP = [list(input()) for i in range(N)]
ch = [[0] * M for _ in range(N)]
res = 0
for i in range(N):
    for j in range(M):
        if ch[i][j] == 0 and MAP[i][j] == '#':
            q.append((i, j))
            BFS()
            res += 1

print(res)

"""
2
4 4
#.#.
.#.#
#.##
.#.#
3 5
###.#
..#..
#.###
>
6
3
------------------


"""
