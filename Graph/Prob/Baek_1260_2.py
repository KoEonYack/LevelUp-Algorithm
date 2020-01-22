"""
    @ 1260. DFS와 BFS
    @ Prob. https://www.acmicpc.net/problem/1260
     Ref. https://home-body.tistory.com/48
    @ Algo: DFS, BFS
    @ Start day: 20. 01. 22
    @ End day: 20. 01. 22
"""

from collections import deque
import sys

sys.setrecursionlimit(1000000)


def DFS(v):
    print(str(v), end=" ")
    if v == M:
        return
    else:
        for i in range(1, N+1):
            if MAP[v][i] == 1 and check[i] is False:
                check[i] = True
                DFS(i)

def BFS(v):
    Q = deque([])
    Q.append(v)
    #check_BFS[v] = True

#    while Q:
#        x = Q.popleft()
#        print(x, end=" ")
#        for i in range(1, N+1):
#            print(check_BFS)
#            if MAP[v][i] == 1 and check_BFS[i] is False:
#                check_BFS[i] = True
#                Q.append(i)

    while Q:
        x = Q.popleft()
        if check_BFS[x] is False:
            check_BFS[x] = True
            print(x, end=" ")
            for i in range(1, N+1):
                if MAP[x][i] == 1 and check_BFS[i] is False:
                    Q.append(i)


# 정점, 간선, 탐색 시작 vertex
N, M, V = map(int, input().split())
MAP = [[0] * (N+1) for _ in range(N+1)]
check = [False] * (N+1)
check_BFS = [False] * (N+1)

for i in range(M):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1


check[V] = True
DFS(V)
print()
BFS(V)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
>
1 2 4 3 - DFS
1 2 3 4 - BFS


5 5 3
5 4
5 2
1 2
3 4
3 1
>
3 1 2 5 4
3 1 4 2 5
"""