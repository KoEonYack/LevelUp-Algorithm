"""
    @ 7562. 나이트의 이동 [런타임에러]
    @ Prob. https://www.acmicpc.net/problem/7562
     Ref. https://lmcoa15.tistory.com/21 
    @ Algo: DFS
    @ Start day: 19. 12. 27.
    @ End day:
"""

from collections import deque

dx = [-2, -1, 1, 2, -2, -1, 2, 1]
dy = [-1, -2, -2, -1, 1, 2, 1, 2]
N = int(input())
for _ in range(N):
    l = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    q = deque()
    q.append([startY, startX])

    while q:
        y, x = q.popleft()

        if y == endY and x == endX:
            print(visited[y][x])
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < l and 0 <= nx < l:
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append([ny, nx])


"""
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

>>>>>
5
28
0
"""