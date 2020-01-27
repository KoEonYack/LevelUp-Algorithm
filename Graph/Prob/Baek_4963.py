"""
    @ 4963. 섬의 개수
    @ Prob. https://www.acmicpc.net/problem/4963
     Ref.
    @ Algo: DFS
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""

import sys
sys.setrecursionlimit(1000000)

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [-1, 0, 1, -1, 0, 1, 1, -1]

def DFS(y, x):
    check[y][x] = True
    for i in range(8):
        nx, ny = x+dx[i], y+dy[i]
        if nx >= 0 and nx < W and ny >= 0 and ny < H:
            if MAP[ny][nx] == 1 and check[ny][nx] is False:
                DFS(ny, nx)

check = []
MAP = []
ans = 0
while True:
    W, H = map(int, input().split()) # W, H
    if W == 0 and H == 0: break
    MAP = []
    for _ in range(H):
        MAP.append(list(map(int, input().split())))

    ans = 0
    check = [[False] * W for _ in range(H)]
    for i in range(W):     # 가로
        for j in range(H): # 세로
            if MAP[j][i] == 1 and check[j][i] is False:
                DFS(j, i)
                ans += 1
    print(ans)


"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
>
0
1
1
3
1
9
"""

