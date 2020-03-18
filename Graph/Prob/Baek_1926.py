"""
    @ Baek 1926. 그림
    @ Prob. https://www.acmicpc.net/problem/1926
     Ref.
    @ Algo: 그래프(BFS)
    @ Start day: 20. 03. 18.
    @ End day: 20. 03. 18.
"""

from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS():
    t = 1
    q.append((i, j))
    check[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = 1
                q.append((nx, ny))
                t += 1
    return t


# N: 세로 M: 가로
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]

q = deque()

num_of_pic = 0
maxV = 0
for i in range(N):
    for j in range(M):
        if check[i][j] == 0 and MAP[i][j] == 1:
            num_of_pic += 1
            ret = BFS()
            if ret > maxV: maxV = ret

print(num_of_pic)
print(maxV)


"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
>
4
9
"""