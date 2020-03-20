"""
    @ 16940. BFS 스페셜 저지
    @ Prob. https://www.acmicpc.net/problem/16940
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 02. 16.
    @ End day: 20. 02. 16.
"""

from collections import deque


N = int(input())
MAP = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    MAP[u].append(v)
    MAP[v].append(u)

checkSeqArr = list(map(int, input().split()))
checkSeqArr = [x-1 for x in checkSeqArr]
order = [0] * N

for i in range(N):
    order[checkSeqArr[i]] = i

for i in range(N):
    MAP[i].sort(key=lambda x: order[x])

bfs_order = []
q = deque()
check = [False] * N
q.append(0)
check[0] = True
while q:
    x = q.popleft()
    bfs_order.append(x)
    for y in MAP[x]:
        if check[y] is False:
            check[y] = True
            q.append(y)

ok = True
for i in range(N):
    if bfs_order[i] != checkSeqArr[i]:
        ok = False

print(1 if ok else 0)


"""
4
1 2
1 3
2 4
1 2 3 4
>
1
-------------
4
1 2
1 3
2 4
1 3 2 4
>
1
--------------
4
1 2
1 3
2 4
1 2 4 3
>
0
"""