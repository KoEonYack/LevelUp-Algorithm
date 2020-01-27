"""
    @ 10451. 순열 사이클
    @ Prob. https://www.acmicpc.net/problem/10451
     Ref.
    @ Algo: DFS
    @ Start day: 20. 01. 27.
    @ End day: 20. 01. 27.
"""

import sys
input = sys.stdin.readline

def DFS(v):
    check[v] = True
    for j in range(N+1):
        if MAP[v][j] == 1 and check[j] is False:
            DFS(j)

tSet = int(input())
MAP = []
check = []
for _ in range(tSet):
    N = int(input())
    MAP = [[0]*(N+1) for _ in range(N+1)]
    ans = 0
    check = [False] * (N+1)
    inputArr = list(map(int, input().split()))
    for i in range(N):
        MAP[i+1][inputArr[i]] = 1

    for i in range(N+1):
        if check[i] is False:
            DFS(i)
            ans += 1
    print(ans-1)

"""
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
>
3
7
"""