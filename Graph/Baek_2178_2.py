"""
    @ 2178. 미로탐색
    @ Prob. https://www.acmicpc.net/problem/2178
     Ref. https://j-remind.tistory.com/52
    @ Algo: DFS
    @ Start day: 20. 01. 22
    @ End day:
"""

import sys
sys.setrecursionlimit(1000000)

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    if x == M-1 and y == N-1:
        pass
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or yy < 0 or xx >= M or yy >= N:
                continue
            if MAP[xx][yy] == 0 and check[xx][yy] == 0:
                check[xx][yy] += 1
                DFS(xx, yy)
                check[xx][yy] = False


N, M = map(int, input().split())
check = [[0] * M for _ in range(N)]
MAP = []

for i in range(N):
    inputStr = input()
    inputArr = list(inputStr)
    list_a = [int(i) for i in inputArr]
    MAP.append(list_a)

DFS(0, 0)


"""
4 6
101111
101010
101011
111011
>
15
"""