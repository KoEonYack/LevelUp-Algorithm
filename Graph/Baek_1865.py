"""
    @ Baek 1865. 웜홀 [TODO]
    @ Prob. https://www.acmicpc.net/problem/1865
     Ref.
    @ Algo: 최단거리 (벨만포드)
    @ Start day: 20. 07. 15.
    @ End day: 20. 07. 15.
"""


def bell():
    cycle = False
    for i in range(1, N):
        for j in range(1, N):
            for x, c in edges[j]:
                if dist[j] != float('inf') and dist[x] > dist[j] + c:
                    dist[x] = dist[j] + c
                    cycle = True

    return cycle

for _ in range(int(input())):
    N, M, W = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    dist = [float('inf')] * (N+1)

    for i in range(M):
        s, e, c = map(int, input().split())
        edges[s].append((e, c))
        edges[e].append((s, c))

    for i in range(W):
        s, e, c = map(int, input().split())
        edges[s].append((e, -c))

    dist[1] = 0
    print('YES' if bell() else 'NO')


"""
2
3 3 1
1 2 2
1 3 4
2 3 1
3 1 3
3 2 1
1 2 3
2 3 4
3 1 8
>
NO
YES
"""