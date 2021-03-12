"""
    @ Baek 2252. 줄 세우기
    @ Prob. https://www.acmicpc.net/problem/2252
     Ref.
    @ Algo: BFS (위상정렬)
    @ Start day: 20. 07. 06.
    @ End day: 20. 07. 06.
"""


from collections import deque


def BFS():
    while q:
        v = q.popleft()
        print(v, end=" ")
        for vv in MAP[v]:
            indeg[vv] -= 1
            if indeg[vv] == 0:
                q.append(vv)


N, M = map(int, input().split())
MAP = [[] for _ in range(N+1)]
indeg = [0] * (N+1)

for _ in range(M):
    s, e = map(int, input().split())
    MAP[s].append(e)
    indeg[e] += 1

q = deque()

for i in range(1, N+1):
    if indeg[i] == 0:
        q.append(i)

BFS()





"""
3 2
1 3
2 3
>
1 2 3


--------


4 2
4 2
3 1
>
4 2 3 1

"""
