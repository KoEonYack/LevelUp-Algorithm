"""
    @ Baek 11657. 최소비용 구하기
    @ Prob. https://www.acmicpc.net/problem/11657
     Ref.
    @ Algo: 최단거리 (벨만포드)
        - 벨만포드의 특징인 음수 싸이클을 고려한 문제
    @ Start day: 20. 07. 09.
    @ End day: 20. 07. 09.
"""

def bellman():
    flag = False
    for i in range(V-1):
        for j in range(E):
            From = edges[j][0]
            to = edges[j][1]
            cost = edges[j][2]
            if dist[From] != inf and dist[to] > dist[From] + cost:
                dist[to] = dist[From] + cost
                flag = True
    return flag

V, E = map(int, input().split())

edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])

inf = 987654321
dist = [inf] * (V+1)

dist[1] = 0
bellman()
# dist[1] = 0

if bellman() is True:
    print(-1)
else:
    for i in range(2, len(dist)):
        if dist[i] == inf:
            print(-1)
        else:
            print(dist[i])

"""
1 1
1 1 1

3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
>
4
3
----------------------
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2
>
-1
---------------------
3 2
1 2 4
1 2 3
>
3
-1
"""