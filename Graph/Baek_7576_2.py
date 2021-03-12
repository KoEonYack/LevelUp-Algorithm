"""
    @ 7576. 토마토
    @ Prob. https://www.acmicpc.net/problem/7576
     Ref.
    @ Algo: BFS
    @ Start day: 20. 07. 04
    @ End day: 20. 07. 04
"""

def BFS():
    ans = 0

    while q:
        y, x = q.popleft()
        for nx, ny in dirs:
            nx = nx + x; ny = ny + y
            if 0 <= nx < N and 0 <= ny < M and MAP[ny][nx] == 0:
                MAP[ny][nx] = MAP[y][x] + 1
                q.append((ny, nx))
                if MAP[ny][nx] > ans: ans = MAP[ny][nx]

    return ans


from collections import deque

# N:가로  M: 세로
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(M)]
q = deque()

# for i in range(M):
#     print(MAP[i])

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(M):
    for j in range(N):
        if MAP[i][j] == 1:
            q.append((i, j))

ans = BFS()

# for i in range(M):
#     print(MAP[i])
# print("===============")

flag = True
for i in range(M):
    for j in range(N):
        if MAP[i][j] == 0:
            flag = False

if flag is False:
    print(-1)
else:
    if ans == 0:
        print(0)
    else:
        print(ans-1)


"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
>
8
------------
6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

"""