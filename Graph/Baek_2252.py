"""
    @ Baek 2252. 줄 세우기
    @ Prob. https://www.acmicpc.net/problem/2252
     Ref.
    @ Algo: BFS (위상정렬)
    @ Start day: 20. 03. 20.
    @ End day: 20. 03. 20.
"""

from collections import deque

N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]
ind = [0] * (N+1) # indegree


for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)
    ind[e] += 1

q = deque()
for i in range(1, N+1):
    if ind[i] == 0:
        q.append(i)

# for a in MAP:
#     print(a)

while q:
    a = q.popleft()
    print(a, end=" ")
    for i in range(len(MAP[a])):
        y = MAP[a][i]
        ind[y] -= 1
        if ind[y] == 0:
            q.append(y)

"""
3 2
1 3
2 3
>
1 2 3
-----------
4 2
4 2
3 1
>
4 2 3 1
"""




