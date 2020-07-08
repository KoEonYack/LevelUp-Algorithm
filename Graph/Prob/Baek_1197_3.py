"""
    @ Baek 1197. 최소 스페닝 트리
    @ Prob. https://www.acmicpc.net/problem/1197
     Ref.
    @ Algo: 최소 스페닝 트리 (크루주칼)

    @ Start day: 20. 07. 07.
    @ End day: 20. 07. 07.
"""

def find(u):
    if u == parent[u]:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def merge(u, v):
    u = find(u)
    v = find(v)
    parent[v] = u


V, E = map(int, input().split())
parent = [0] * 10001

for i in range(1, V+1):
    parent[i] = i

v = []
for i in range(E):
    s, e, c = map(int, input().split())
    v.append((s, e, c))

v.sort(key=lambda x: x[2])

ans = 0
for val in v:
    if find(val[1]) != find(val[0]) :
        merge(val[1], val[0])
        ans += val[2]

print(ans)

"""
3 3
1 2 1
2 3 2
1 3 3
>
3

"""