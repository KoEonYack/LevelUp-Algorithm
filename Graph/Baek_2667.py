"""
    @ 2667. 미로탐색
    @ Prob. https://www.acmicpc.net/problem/2667
     Ref. https://sejinik.tistory.com/59
    @ Algo: DFS
    @ Start day: 19. 12. 26.
    @ End day: 19. 12. 26.
"""

import sys
sys.setrecursionlimit(1000000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    visited[x][y] = True
    numArr[cnt] += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny] is False and arr[nx][ny] > 0:
                DFS(nx, ny)


def solution():
    global cnt

    for i in range(N):
        for j in range(N):
            if visited[i][j] is False and arr[i][j] > 0:
                DFS(i, j)
                cnt += 1


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * 30 for _ in range(30)]
numArr = [0] * 1010
cnt = 0
solution()
print(cnt)
numArr.sort()
for i in range(len(numArr)-cnt, len(numArr)):
    print(numArr[i])


"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

> 
"""


