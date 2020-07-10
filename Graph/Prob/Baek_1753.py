"""
    @ Baek 1753. 최단경로
    @ Prob. https://www.acmicpc.net/problem/1753
     Ref. https://pacific-ocean.tistory.com/281 Refes
    @ Algo: 최단거리 (다익스트라)
    @ Start day: 20. 07. 10.
    @ End day: 20. 07. 10.
"""

import heapq

def dijkstra(start):
    DP[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for nn, nw in a[n]:
            nw = nw + w

inf = 987654321

# start, end, weight
V, E = map(int, input().split())
start = int(input())
DP = [inf] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append((v, w))

heap = []
dijkstra(k)
for i in DP[1:]:
    print(i if i != inf else: "INF")





"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
>
0
2
3
7
INF
"""

