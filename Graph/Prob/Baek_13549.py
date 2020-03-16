"""
    @ 13549. 숨바꼭질 3
    @ Prob. https://www.acmicpc.net/problem/13549
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 13.
    @ End day: 20. 03. 13.
"""

from collections import deque

q = deque()
MAX_SIZE = 100000
check = [False] * (MAX_SIZE+1)
dist = [-1] * (MAX_SIZE + 1)

N, K = map(int, input().split())
q.append(N)
dist[N] = 0
check[N] = True
while q:
    curr = q.popleft()
    if curr == K:
        break

    if curr*2 <= MAX_SIZE and check[curr*2] is False:
        q.appendleft(curr*2)
        dist[curr*2] = dist[curr]
        check[curr*2] = True

    for next in (curr-1, curr+1):
        if 0 <= next <= MAX_SIZE and check[next] is False:
            q.append(next)
            dist[next] = dist[curr] + 1
            check[next] = True

print(dist[K])

"""
5 17
>
2   
"""
