"""
    @ Baek 1766. 문제집
    @ Prob. https://www.acmicpc.net/problem/1766
     Ref.
    @ Algo: BFS (위상정렬)
    @ Start day: 20. 03. 20.
    @ End day: 20. 03. 20.
"""

import heapq

N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]
ind = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)
    ind[e] += 1

hq = []
for i in range(1, N+1):
    if ind[i] == 0:
        heapq.heappush(hq, i)

res = []
while hq:
    x = heapq.heappop(hq)
    print(x, end=" ")
    #res.append(x)
    for num in MAP[x]:
        ind[num] -= 1
        if ind[num] == 0:
            heapq.heappush(hq, num)

#for i in res:
#    print(i, end=" ")

"""
4 2
4 2
3 1
>
3 1 4 2
"""