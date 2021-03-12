"""
    @ 13913. 숨바꼭질 4
    @ Prob. https://www.acmicpc.net/problem/13913
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 03. 13.
    @ End day: 20. 03. 13.
"""

from collections import deque
import sys

sys.setrecursionlimit(1000000000)
MAX_SIZE = 100000
check = [False] * (MAX_SIZE + 1)
dist = [0] * (MAX_SIZE + 1)
move_to = [0] * (MAX_SIZE + 1)
q = deque([])

N, K = map(int, input().split())
q.append(N)
check[N] = True
dist[N] = 0

while q:
    now = q.popleft()
    if now == K:
        print(dist[now])
        p = []
        while now != N:
            p.append(now)
            now = move_to[now]
        p.append(N)
        p.reverse()
        print(' '.join(map(str, p)))
        break
    for curr in (now-1, now+1, now*2):
        if 0 <= curr <= MAX_SIZE and check[curr] is False:
            q.append(curr)
            check[curr] = True
            dist[curr] = dist[now] + 1
            move_to[curr] = now


#def print_location(n, m):
#    if n != m:
#        print_location(n, move_to[m])
#    print(m, end=" ")

#print(dist[K])
#print_location(N, K)

"""
5 17
>
4
5 10 9 18 17
or
4
5 4 8 16 17
"""



