"""
    @ Baek 1916. 최소비용 구하기
    @ Prob. https://www.acmicpc.net/problem/1916
     Ref.
    @ Algo: 최단거리 (벨만포드)
        - 출발도시에서 도착도시 가는데 최소비용
    @ Start day: 20. 07. 08.
    @ End day: 20. 07. 08.
"""

N = int(input()) # 도시의 갯수
M = int(input()) # 버스의 갯수
edges = []
for _ in range(M): # 버스의 정보(출발도시, 도착도시, 버스 비용)
    s, e, w = map(int, input().split())
    edges.append([s, e, w])

inf = 999999999
dist = [inf] * (N+1)
#for i in range(1, N+1):
#    dist[i] = inf

start, end = map(int, input().split())
dist[start] = 0

for i in range(N-1):
    for j in range(M):
        From = edges[j][0] # from은 파이썬의 예약어라 대문자 From 사용
        to = edges[j][1]
        cost = edges[j][2]
        if dist[From] != inf and dist[to] > dist[From] + cost:
            dist[to] = dist[From] + cost

print(dist[end])




"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
>
4
"""