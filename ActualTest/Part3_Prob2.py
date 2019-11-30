'''
    Part3 - Prob2. : DFS
    Connected Component
    print(solution(6, [[1,2],[2,3],[4,5]]))
'''

import sys
sys.setrecursionlimit(30000)


def dfs(x, check, Vertex):
    check[x] = True
    for i in Vertex[x]:
        if check[i] is False:
            dfs(i, check, Vertex)

def solution(VertexNum, bridges):
    ans = 0

    Vertex = [[] for _ in range(VertexNum + 1)]
    check = [False] * (VertexNum + 1)

    for _ in range(VertexNum): # vertex에 edge를 추가
        # 값 읽으셔야지
        for bridge in bridges:
            Vertex[bridge[0]].append(bridge[1])
            Vertex[bridge[1]].append(bridge[0])

    for i in range(1, VertexNum+1): # DFS 수행
        if check[i] is False:
            dfs(i, check, Vertex)
            ans += 1
    
    return ans


#print(solution(5, [[1,2],[2,3],[4,5]]))
print(solution(6, [[1,2],[2,3],[4,5]]))