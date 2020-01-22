'''
    @ 1260. DFS와 BFS
    @ Prob. https://www.acmicpc.net/problem/1260
    @ Ref. https://jun-itworld.tistory.com/18
    @ Algo: DFS, BFS
    @ Start day: 19. 09. 18
    @ End day:
'''

def dfs(v):
    print(str(v) + " ")
    visit[v] = 1
    for i in range(1, N+1):
        if (visit[i] is 1) or (matrix[v][i] is 0):
            continue
        dfs(i)

def bfs(startV):
    result = ""
    q = []
    q.append(startV)
    visit[startV] = 0

    while len(q) is not 0:
        v = q[0]
        q.pop(0)
        result += str(v) + " "

        for i in range(1, N+1): # 1 ~ N
            if (visit[i] is 0) or (matrix[v][i] is 0):
                continue
            q.append(i)
            visit[i] = 0

    return result


# N: 정점의 갯수, N: 간선의 갯수, V: 탐색을 시작할 정점의 번호
N, M, V = map(int, input().split())
matrix = [[0] * (N+1) for _ in range(N+1)]
visit = [1] * (N+1)
resultDFS = ""

for _ in range(M):
    fromTo = list(map(int, input().split()))
    matrix[fromTo[0]][fromTo[1]] = 1
    matrix[fromTo[1]][fromTo[0]] = 1

dfs(V)
print(bfs(V))


"""
4 5 1
1 2
1 3
1 4
2 4
3 4
>
1 2 4 3 - DFS
1 2 3 4 - BFS


5 5 3
5 4
5 2
1 2
3 4
3 1
>
3 1 2 5 4
3 1 4 2 5
"""



