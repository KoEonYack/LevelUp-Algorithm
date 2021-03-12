'''
    @ 2178. 미로탐색
    @ Prob. https://www.acmicpc.net/problem/2178
     Ref. https://j-remind.tistory.com/52
    @ Algo: BFS
    @ Start day: 19. 09. 19
    @ End day:
'''

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
MAP = []
visited = [[0] * M for _ in range(N)]

for i in range(N):
    MAP.append([int(i) for i in list(input())])

q = deque()
q.append((0, 0))
visited[0][0] = 1

while q:
    x, y = q.popleft()
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx >= 0 and xx < N and yy >= 0 and yy < M:
            if (visited[xx][yy] is 0) and (MAP[xx][yy] is 1):
                visited[xx][yy] = visited[x][y] + 1
                q.append((xx, yy))

"""
4 6
101111
101010
101011
111011

>> 15
"""