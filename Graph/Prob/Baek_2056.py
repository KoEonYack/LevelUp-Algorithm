"""
    @ Baek 2056. 작업
    @ Prob. https://www.acmicpc.net/problem/2056
     Ref.
    @ Algo: BFS (위상정렬)
    @ Start day: 20. 03. 20.
    @ End day: 20. 03. 20.
"""

from collections import deque

N = int(input())
MAP = []
ind = [0] * (N+1)
time = [0] * (N+1)
for i in range(1, N+1):
    t, m, *jobs = map(int, input().split())
    time[i] = t
    MAP.append(jobs)
    ind[i] = m


for a in MAP:
    print(a)
print(ind)

q = deque()
for i in range(1, N):
    if ind[i] == 0:
        q.append(i)

while q:
    x = q.popleft()
    print(x, end=" ")
    for num in MAP[x]:
        ind[num] -= 1
        if ind[num] == 0:
            print("here")
            q.append(num)


"""
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6
>
23
"""