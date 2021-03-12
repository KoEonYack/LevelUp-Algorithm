"""
    @ Baek 2606. 바이러스
    @ Prob. https://www.acmicpc.net/problem/2606
     Ref.
    @ Algo: Union Find
    @ Start day: 20. 03. 26.
    @ End day: 20. 03 26.
"""


def Union(x, y):
    x = Find(x)
    y = Find(y)

    if x == y:
        return

    if rank[x] < rank[y]: x, y = y, x
    parent[y] = x
    if rank[x] == rank[y]:
        rank[x] = rank[y] + 1

def Find(x):
    if x == parent[x]:
        return x
    else:
        y = Find(parent[x])
        parent[x] = y
        return y


N = int(input())
M = int(input())

parent = [0] * (N+1)
rank = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    x, y = map(int, input().split())
    Union(x, y)

count = 0
root = Find(1)
for i in range(2, N+1):
    if Find(i) == root:
        count += 1

print(count)



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