"""
    @ Baek 2606. 바이러스
    @ Prob. https://www.acmicpc.net/problem/2606
     Ref.
    @ Algo: BFS
    @ Start day: 20. 03. 19.
    @ End day: 20. 03 19.
"""

from collections import deque

N = int(input())
check = [0] * (N+1)
Computer = [[] for _ in range(N+1)]

for i in range(int(input())):
    a, b = map(int, input().split())
    Computer[a].append(b)
    Computer[b].append(a)

check[1] = 1
q = deque([1])
while q:
    x = q.popleft()
    for i in range(len(Computer[x])):
        if check[Computer[x][i]] == 0:
            q.append(Computer[x][i])
            check[Computer[x][i]] = 1

print(sum(check) - 1)


"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
>
4
"""

