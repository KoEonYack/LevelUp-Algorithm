"""
    @ Baek 4108 지뢰찾기
    @ Prob. https://www.acmicpc.net/problem/4108
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 03. 09.
    @ End day: 20. 03. 09.
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    # 세로, 가로
    N, M = map(int, input().split())
    if N == M == 0:
        break

    arr = []
    for i in range(N):
        arr.append(list(input()))

    for a in arr:
        print(a)

    DP = [['*']*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                cnt = 0
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if 0 <= xx <= M and 0 <= yy <= N:
                        if DP[yy][xx] == "*":
                            cnt += 1
                if cnt >= 0:
                    for k in range(4):
                        xx = i + dx[k]
                        yy = j + dy[k]
                        if 0 <= xx <= M and 0 <= yy <= N:
                            DP[xx][yy] = cnt

    for i in range(1, N+1):
        for j in range(1, M+1):
            print(DP[i][j], end=" ")
        print()


"""
3 2
..
.*
..
0 0

5 5
*.*.*
..*..
*****
.....
..**.
0 0
>
11
1*
11
*3*3*
36*63
*****
24553
01**1
"""