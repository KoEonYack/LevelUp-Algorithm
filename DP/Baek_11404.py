"""
    @ 11404. 플로이드
    @ Prob. https://www.acmicpc.net/problem/11404
     Ref. https://claude-u.tistory.com/334
    @ Algo: DP
    @ Start day: 20. 01. 20.
    @ End day: 20. 01. 20.
"""

N = int(input())
M = int(input())
dis = [[100001] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dis[i][i] = 0

for i in range(M):
    A, B, C = map(int, input().split())
    dis[A][B] = min(dis[A][B], C)


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dis[i][j] > dis[i][k] + dis[k][j]:
                dis[i][j] = dis[i][k] + dis[k][j]

for row in dis[1:]:
    for col in row[1:]:
        if col == 100001:
            print(0, end=" ")
        else:
            print(col, end=" ")
    print()


"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
>
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
"""