"""
    @ Baek 16953. A → B
    @ Prob. https://www.acmicpc.net/problem/16953
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

A, B = map(int, input().split())

q = deque()
q.append((A, 1))

while q:
    x, t = q.popleft()
    if x == B:
        print(t)
        exit()

    if x*2 <= B:
        q.append((x*2, t+1))
    x = int(str(x) + "1")
    if x <= B:
        q.append((x, t+1))

print(-1)

"""
2 162
>
5
"""