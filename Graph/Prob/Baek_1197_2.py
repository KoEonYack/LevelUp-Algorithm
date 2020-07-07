"""
    @ Baek 1197. 최소 스페닝 트리
    @ Prob. https://www.acmicpc.net/problem/1197
     Ref.
    @ Algo: 최소 스페닝 트리
        1. 그래프에서 아무 정점을 선택한다.
        2. 선택한 정점과 선택하지 않은 정점을 연결하는 간선중에 최솟값을 고른다.
            이 간선을 (u, v)라고 한다.
        3. 선택한 간선을 MST에 추가하고 v를 선택한다.
        4. 모든 정점을 선택하지 않으면 2번 단계로 간다.

        PriorityQueue:
            put()
            get()
    @ Start day: 20. 07. 07.
    @ End day: 20. 07. 07.
"""


import heapq

def MST(start):
    visit[start] = True
    total_w = 0
    h = []

    for i in range(len(MAP[start])):
        next = MAP[start][i][1]
        next_cost = MAP[start][i][0]
        heapq.heappush(h, (next_cost, next))


    while h:
        curr_cost, curr = heapq.heappop(h)

        if visit[curr] == True: continue

        visit[curr] = True
        total_w += curr_cost
        # print(curr_cost)
        for i in range(len(MAP[curr])):
            next = MAP[curr][i][1]
            next_cost = MAP[curr][i][0]
            # print(next, next_cost)
            heapq.heappush(h, (next_cost, next))


    return total_w


V, E = map(int, input().split())
MAP = [[] for _ in range(10001)]
visit = [False] * 10001
for _ in range(E):
    s, e, c = map(int, input().split())
    MAP[s].append((c, e))
    MAP[e].append((c, s))

print(MST(1))


"""
3 3
1 2 1
2 3 2
1 3 3
>
3

"""