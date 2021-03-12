"""
    @ 11724. 연결 요소
    @ Prob. https://www.acmicpc.net/problem/11724
     Ref.   https://salguru.tistory.com/133
            https://rebas.kr/653 (Python)
    @ Algo: DFS
    @ Start day: 20. 01. 26.
    @ End day: 20. 01. 26.
"""

import sys
sys.setrecursionlimit(1000000)


def DFS(v):
    check[v] = True
    for i in range(1, N+1):
        if MAP[v][i] == 1 and check[i] is False:
            check[i] = True
            DFS(i)


# N 정점의 갯수, M : 간선의 갯수
N, M = map(int, input().split())
check = [False] * (N+1)
MAP = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    MAP[start][end] = 1
    MAP[end][start] = 1

ans = 0

for i in range(1, N+1):
    if check[i] is False:
        DFS(i)
        ans += 1

print(ans)

"""
6 5
1 2
2 5
5 1
3 4
4 6
>
2


6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
>
1
"""