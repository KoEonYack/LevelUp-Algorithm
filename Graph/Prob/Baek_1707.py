"""
    @ 1707. 이분 그래프
    @ Prob. https://www.acmicpc.net/problem/1707
     Ref.
    @ Algo: DFS
    @ Start day: 20. 02. 15.
    @ End day: 20. 02. 15.
"""

import sys
sys.setrecursionlimit(1000000)


def DFS(x, c):
    color[x] = c
    for y in MAP[x]:
        if color[y] == 0:
            if not DFS(y, 3 - c):
                return False
        elif color[y] == color[x]:
            return False
    return True


T = int(sys.stdin.readline())
for _ in range(T):
    # N: 정점의 갯수 M: 간선의 갯수
    N, M = map(int, sys.stdin.readline().split())
    MAP = [[] for _ in range(N)]
    color = [0] * N

    for _ in range(M):
        start, end = map(int, sys.stdin.readline().split())
        MAP[start-1].append(end-1)
        MAP[end-1].append(start-1)



    ans = True
    for i in range(N):
        if color[i] == 0:
            if not DFS(i, 1):
                ans = False

    print("YES" if ans else "NO")


"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
>
YES
NO
"""