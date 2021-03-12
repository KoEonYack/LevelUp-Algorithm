"""
    @ 14226. 이모티콘
    @ Prob. https://www.acmicpc.net/problem/14226
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 13.
    @ End day: 20. 03. 13.
"""

from collections import deque

MAX_SIZE = 1001
q = deque()
dist = [[-1] * MAX_SIZE for _ in range(MAX_SIZE)]
q.append((1, 0))
dist[1][0] = 0
N = int(input())

while q:
    s, c = q.popleft()
    if dist[s][s] == -1:
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    if s+c <= N and dist[s+c][c] == -1:
        dist[s+c][c] = dist[s][c] + 1
        q.append((s+c, c))
    if s-1 >= 0 and dist[s-1][c] == -1:
        dist[s-1][c] = dist[s][c] + 1
        q.append((s-1, c))

ans = -1
for i in range(0, N+1):
    if dist[N][i] != -1:
        if ans == -1 or ans > dist[N][i]:
            ans = dist[N][i]

print(ans)

"""
2
>
2
----------
4
>
4
----------
6
>
5
"""


