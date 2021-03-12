"""
    @ 1197. 최소 스패닝 트리
    @ Prob. https://www.acmicpc.net/problem/1197
     Ref.
    @ Algo: Prime MST
    @ Start day: 20. 01. 23.
    @ End day: 20. 01. 23
"""
from queue import PriorityQueue

V, E = map(int, input().split())
MAP = [[0]*(V+1) for _ in range(V+1)]
check = [False] * (V+1)
Q = PriorityQueue()

for i in range(E):
    start, end, W = map(int, input().split())
    MAP[start][end] = W
    MAP[end][start] = W

Q.put((1, 0))
res = 0
while not Q.empty():
    v, cost = Q.get()
    if check[v] is False:
       res += cost
       check[v] = True
       for i in range(1, E+1):
           if MAP[v][i] > 0:
               Q.put((i, MAP[v][i]))

print(res)


"""
100,000 * 100,000

3 3
1 2 1
2 3 2
1 3 3
>
3
"""