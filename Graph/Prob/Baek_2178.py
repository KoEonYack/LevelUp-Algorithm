'''
    @ 2178. 미로탐색
    @ Prob. https://www.acmicpc.net/problem/2178
     Ref. https://j-remind.tistory.com/52
    @ Algo: BFS
    @ Start day: 19. 09. 19
    @ End day:
'''

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
MAP = []

visited = [[0] * M for _ in range(N)]

for i in range(N):
    inputStr = input()
    inputArr = list(inputStr)
    list_a = [int(i) for i in inputArr]
    MAP.append(list_a)

arr = []
arr.append((0, 0))
visited[0][0] = 1

while arr:
    x, y = arr.pop(0)
    if x == N-1 and y == M-1:
        print(visited[x][y])
        break
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx >= 0 and xx < N and yy >= 0 and yy < M:
            if (visited[xx][yy] is 0) and (MAP[xx][yy] is 1):
                visited[xx][yy] = visited[x][y] + 1
                arr.append((xx, yy))

"""
4 6
101111
101010
101011
111011

>> 15
"""