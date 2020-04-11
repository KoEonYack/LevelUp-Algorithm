"""
    @ Baek 6189. Munching
    @ Prob. https://www.acmicpc.net/problem/6189
     Ref.
    @ Algo: BFS
    @ Start day: 20. 04. 10.
    @ End day: 20. 04. 10.
"""

def BFS():
    while q:
        y, x = q.popleft()
        for dy, dx in dirs:
            nx = x + dx; ny = y + dy
            if 0 <= ny < N and 0 <= nx < M:
                if ch[ny][nx] == -1 and MAP[ny][nx] != '*':
                    ch[ny][nx] = ch[y][x] + 1
                    q.append((ny, nx))



from collections import deque


# N: 세로 / M: 가로
N, M = map(int, input().split())
MAP = [list(input()) for _ in range(N)]
ch = [[-1] * M for _ in range(N)]
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]
q = deque()
ey = -1; ex= -1
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 'B':
            q.append((i, j))
            ch[i][j] = 0
        elif MAP[i][j] == 'C':
            ey = i; ex = j

BFS()
# for a in ch:
#     print(a)
print(ch[ey][ex])

"""
5 6
B...*.
..*...
.**.*.
..***.
*..*.C
>
9

"""