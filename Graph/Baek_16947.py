"""
    @ 16947. 서울 지하철 2호선
    @ Prob. https://www.acmicpc.net/problem/16947
     Ref.
    @ Algo: 그래프
    @ Start day: 20. 02. 16.
    @ End day: 20. 02. 16.
"""

import sys

sys.setrecursionlimit(10000000)
from collections import deque

n = int(input())
a = [[] for _ in range(n)]
for _ in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

check = [0] * n  # 0: not visited, 1: visited, 2: cycle


def go(x, p):
    # -2: found cycle and not included
    # -1: not found cycle
    # 0~n-1: found cycle and start index

    if check[x] == 1:
        return x

    check[x] = 1
    for y in a[x]:
        if y == p:
            continue
        res = go(y, x)
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2
            if x == res:
                return -2
            else:
                return res
    return -1


go(0, -1)

q = deque()
dist = [-1] * n

for i in range(n):
    if check[i] == 2:
        dist[i] = 0
        q.append(i)
    else:
        dist[i] = -1

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(*dist, sep=' ')

"""
4
1 3
4 3
4 2
1 2
>
0 0 0 0 
---------
51
1 2
2 3
3 4
4 5
5 6
6 7
7 8
8 9
9 10
10 11
11 12
12 13
13 14
14 15
15 16
16 17
17 18
18 19
19 20
20 21
21 22
22 23
23 24
24 25
25 26
26 27
27 28
28 29
29 30
30 31
31 32
32 33
33 34
34 35
35 36
36 37
37 38
38 39
39 40
40 41
41 42
42 43
43 1
11 44
44 45
45 46
46 47
34 48
48 49
49 50
50 51
>
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 2 3 4 1 2 3 4
"""
