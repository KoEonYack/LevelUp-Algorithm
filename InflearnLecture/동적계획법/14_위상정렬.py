"""
    @ 14. 위상정렬
    @ Start day: 20. 01. 21
    @ End day: 20. 01. 21
"""

from collections import deque

Q = []

N, M = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
degree = [0] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    graph[start][end] = 1
    degree[end] += 1

for i in range(1, N+1):
    if degree[i] == 0:
        Q.append(i)

while Q:
    for i in Q:
        tmp = i
        Q.remove(i)
        print(i, end=" ")
        for j in range(1, N + 1):
            if graph[tmp][j] == 1:
                degree[j] -= 1
                if degree[j] == 0:
                    Q.append(j)

"""
    now = Q[0]
    Q.remove(Q.index(0))
    for i in range(1, N+1):
        if graph[now][i] == 1:
            degree[i] -= 1
            if degree[i] == 0:
                Q.append(i)
"""




"""
6 6
1 4
5 4
4 3
2 5
2 3
6 2
>
1 6 2 5 4 3
-----------------------------
3 2
1 3
2 3
>
1 2 3
-----------------------------
4 2
4 2
3 1
>
3 4 1 2 
"""
