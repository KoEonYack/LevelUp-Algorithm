'''
    @ 1260. DFS와 BFS
    @ Prob. https://www.acmicpc.net/problem/1260
     Ref. https://jun-itworld.tistory.com/18
          https://jun-itworld.tistory.com/18
    @ Algo: DFS, BFS
    @ Start day: 19. 09. 18
    @ End day:
'''
import Queue

def dfs():
    pass

def bfs(startV):
    result = []
    q = []
    q.append(startV)
    visit[startV] = 0

    while len(q) is 0:
        v = q[0]
        q.pop(0)
        result.append(v)

        for i in range(1, N+1): # 1 ~ N
            if (visit[i] is 0) or map[v][i] is 0:
                continue
            q.append(i)
            visit[i] = 0


# N: 정점의 갯수, N: 간선의 갯수, V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(M):
    fromTo = list(map(int, input().split()))
    matrix[fromTo[0]][fromTo[1]] = 1
    matrix[fromTo[1]][fromTo[0]] = 1

print(bfs(V))


