"""
    @ 5567. 결혼식
    @ Prob. https://www.acmicpc.net/problem/5567
     Ref.https://claude-u.tistory.com/192
    @ Algo: DFS
    @ Start day: 20. 01. 14
    @ End day: 20. 01. 14
"""

import sys, collections

def bfs(start):
    q = collections.deque()
    q.append(start)
    
    while q:
        node = q.popleft()

        for next in v[node]:
            if check[next] == 0:
                # 다음 방문할 정점의 거리를 현재 정점까지의 거리 +1이됩니다.
                check[next] = check[node] + 1
                q.append(next)

n = int(input())
m = int(input())

v = [[] for _ in range(n+1)]
check = [0] * (n+1) # 시작 정점으로 부터의 거리 정보를 담은 리스트

# 양방 그래프 제작
for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b)
    v[b].append(a)

check[1] = 1
bfs(1)

result = 0
for i in range(2, n+1):
    if check[i] == 2 or check[i] == 3:
        result += 1

print(result)

"""
6
5
1 2
1 3
3 4
2 3
4 5
>
3
"""