from sys import stdin
input = stdin.readline

# .         →        ↓       ↘
p_dirs = [[0, 1], [1, 0], [1, 1]]
ans = 0

from itertools import combinations

combinations()

def solution(y, x, p_type):
    global ans

    if y == N - 1 and x == N - 1:
        ans += 1
        return
    # O(V*V)  -> O(V*V*3^V)
    for i, dirs in enumerate(p_dirs):
        #      (가로 -> 세로)      or      (세로 -> 가로)
        if (i == 0 and p_type == 1) or (i == 1 and p_type == 0):
            continue

        # 다음에 놓으려는 파이프 (범위 벗어남 or 벽)
        next_y = y + dirs[0]; next_x = x + dirs[1]
        if next_y >= N or next_x >= N or MAP[next_y][next_x] == 1:
            continue

        # 대각선 파이프 못 놓는 경우
        if i == 2 and (MAP[y][x + 1] == 1 or MAP[y + 1][x] == 1):
            continue

        solution(next_y, next_x, i)


def solution_2():
    # 0. →   1. ↘  2.  ↓
    dp[0][0][1] = 1
    for i in range(2, N):
        if MAP[0][i] == 0:
            dp[0][0][i] = dp[0][0][i-1]

    for r in range(1, N):
        for c in range(1, N):
            if MAP[r][c] == 0 and MAP[r][c-1] == 0 and MAP[r-1][c] == 0:
                # ↘ = [이전 ↘] + [이전 →] +  [이전 ↘]
                dp[1][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

            if MAP[r][c] == 0:
                # → = [이전 →] +  [이전 ↘]
                dp[0][r][c] = dp[0][r][c-1] + dp[1][r][c-1]
                # ↓ = [이전 ↓] + [이전 ↘]
                dp[2][r][c] = dp[2][r-1][c] + dp[1][r-1][c]


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
if N <= 15:
    solution(0, 1, 0)
    print(ans)
else:
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    solution_2()
    print(sum(dp[i][N-1][N-1] for i in range(3)))


"""
3
0 0 0
0 0 0
0 0 0
>
1
-------
4
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
>
3
"""