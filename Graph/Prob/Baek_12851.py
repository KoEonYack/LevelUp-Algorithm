"""
    @ Baek 12851. 숨바꼭질 2
    @ Prob. https://www.acmicpc.net/problem/12851
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

N, K = map(int, input().split())
MAX_SIZE = 100001
S = [[MAX_SIZE, 0] for _ in range(MAX_SIZE)]

q = deque()
q.append(N)
S[N][0] = 0
S[N][1] = 1

while q:
    x = q.popleft()
    for nx in [x*2, x+1, x-1]:
        if 0 <= nx < MAX_SIZE:
            if S[nx][0] == MAX_SIZE:
                q.append(nx)
                S[nx][0] = S[x][0] + 1
                S[nx][1] = S[x][1]
            elif S[nx][0] == S[x][0]:
                S[nx][1] += S[x][1]

print(S[K][0])
print(S[K][1])

"""
5 17
>
4
2
"""
