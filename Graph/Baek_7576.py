'''
    @ 7576. 토마토 - ? s
    @ Prob. https://www.acmicpc.net/problem/7576
     Ref. https://upcount.tistory.com/19
    @ Algo: BFS
    @ Start day: 19. 12. 26.
    @ End day:
'''


import sys
from collections import deque

# input = sys.stdin.readline

M, N = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
unriped = 0
farm = []
tomato = deque([])

for i in range(N):

    farm.append(list(map(int, input().split())))
    for t in range(M):
        if farm[i][t] == 1:
            tomato.append((i, t))
        elif farm[i][t] == 0:
            unriped += 1

days = 1

while tomato:
    t = tomato.popleft()
    x = t[0]
    y = t[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if farm[nx][ny] != 0:
            continue

        farm[nx][ny] = farm[x][y] + 1
        tomato.append((nx, ny))
        days = max(farm[nx][ny], days)
        unriped -= 1

if unriped == 0:
    print(days - 1)
else:
    print(-1)
