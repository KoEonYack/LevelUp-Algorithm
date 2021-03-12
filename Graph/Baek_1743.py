"""
    @ Baek 1743. 음식물 피하기
    @ Prob. https://www.acmicpc.net/problem/1743
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 18.
    @ End day: 20. 03. 18.
"""

from collections import deque
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def BFS():
    q.append((i, j))
    t = 1
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

# N: 세로, M: 가로 K: 음식물 갯수
N, M, K = map(int, input().split())
MAP = [[0] * M for _ in range(N)]
check = [[0] * M for _ in range(N)]
for _ in range(K):
    x, y = map(int, input().split())
    MAP[x-1][y-1] = 1

q = deque()

ans = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == 1 and check[i][j] == 0:
            res = BFS()
            #print(res)
            if res > ans: ans = res

# for a in MAP:
#     print(a)

print(ans)


"""
3 4 5
3 2
2 2
3 1
2 3
1 1
>
4

"""