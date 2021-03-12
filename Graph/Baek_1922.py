"""
    @ Baek 1922. 네트워크 연결
    @ Prob. https://www.acmicpc.net/problem/1922
     Ref.
    @ Algo: Prime
    @ Start day: 20. 03. 23.
    @ End day:
"""

import heapq

def prime(v):
    q = []
    visited[v] = True
    total_cost = 0
    cnt = 1

    for a in adj[v]:
        heapq.heappush(q, a)

    while q:
        cost, v = heapq.heappop(q)
        if not visited[v]:
            visited[v] = True
            cnt += 1
            total_cost += cost
            for a in adj[v]:
                heapq.heappush(q, a)
        if cnt == N:
            return total_cost

N = int(input())
adj = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(int(input())):
    s, e, c = map(int, input().split())
    adj[s].append([c, e])
    adj[e].append([c, s])

print(prime(1))


"""
6
9
1 2 5
1 3 4
2 3 2
2 4 7
5 6 8
3 4 6
3 5 11
4 5 3
4 6 8
>
23
"""
