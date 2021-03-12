"""
    @ Baek 15902 Sheba's Amoebas
    @ Prob. https://www.acmicpc.net/problem/15902
     Ref.
    @ Algo: DFS
    @ Start day: 20. 07. 20.
    @ End day: 20. 07. 20.
"""

def dfs(x, y):
    S[x][y] = ans
    for k in range(8):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and MAP[nx][ny] == '#'  and S[nx][ny] == -1:
            S[nx][ny] = ans
            dfs(nx, ny)


import sys
sys.setrecursionlimit(1000000000)


dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [-1, 1, 0, 1, -1, 1, 0, -1]

# N: 세로  M: 가로
N, M = map(int, input().split())

MAP = [input() for _ in range(N)]
S = [[-1]*M for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if MAP[i][j] == '#' and S[i][j] == -1:
            dfs(i, j)
            ans += 1

print(ans)


"""
12 10
.#####....
#.....#...
#..#..#...
#.#.#.#...
#..#..#...
.#...#....
..###.....
......#...
.##..#.#..
#..#..#...
.##.......
..........
>
4
"""