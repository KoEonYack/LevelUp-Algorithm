"""
    @ Baek 1939 중량제한
    @ Prob. https://www.acmicpc.net/problem/1939
      Ref.
      Ref Prob.
    @ Algo: Binary Search
    @ Start day: 20. 02. 12.
    @ End day: 20. 02. 12.
"""

import sys
sys.setrecursionlimit(100000)


def DFS(v, cost):
    visited[v] = True

    if v == endNode:
        print("true sec")
        return True
    else:
        for i in range(1, N+1):
            if MAP[v][i] >= cost and visited[i] is False:
                DFS(i, cost)
    return False


N, M = map(int, input().split())
MAP = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    i, j, c = map(int, input().split())
    MAP[i][j] = c
    MAP[j][i] = c

startNode, endNode = map(int, input().split())
start = 1
end = 1000000000
ans = 0
visited = []
while start <= end:
    mid = (start + end) // 2
    visited = [False] * (N+1)
    if DFS(startNode, mid): # mid로 갈 수 있다는 소리 그러면 값을 올려보자.
        start = mid + 1
        print("--")
        if ans < mid:
            ans = mid
    else:
        end = mid - 1

print(ans)



"""
3 3
1 2 2
3 1 3
2 3 2
1 3
>
3
"""