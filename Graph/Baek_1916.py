"""
    @ 1916. 최소비용 구하기
    @ Prob. https://www.acmicpc.net/problem/1916
     Ref.
    @ Algo: DFS
    @ Start day: 20. 01. 22.
    @ End day:
"""

import sys

cost = sys.maxsize

def DFS(v, SUM):
    global cost, end
    if v == end:
        if cost > SUM:
            cost = SUM
    else:
        for i in range(1, N+1):
            if MAP[v][i] > 0 and check[i] is False:
                check[i] = True
                DFS(i, SUM+MAP[v][i])
                check[i] = False


N = int(input())
M = int(input())
MAP = [[0] * (N+1) for _ in range(N+1)]
check = [False] * (N+1)
for _ in range(M):
    start, end, W = map(int, input().split())
    MAP[start][end] = W

start, end = map(int, input().split())
check[start] = True
DFS(start, 0)

print(cost)

"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
>
4
---------------------------------
5
8
1 2 12
1 3 6
1 4 10
2 3 2
2 5 2
3 4 3
4 2 2
4 5 5
1 5
>
13
"""


