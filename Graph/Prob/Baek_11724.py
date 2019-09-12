'''
    @ 11724. 연결 요소
    @ Prob. https://www.acmicpc.net/problem/11724
     Ref.   https://salguru.tistory.com/133
            https://rebas.kr/653 (Python)
    @ Algo: DFS
    @ Start day: 19. 09. 03
    @ End day:
'''

import sys
sys.setrecursionlimit(30000)

def dfs(x):
    check[x] = True
    for i in Vertex[x]:
        if check[i] is False:
            dfs(i)

VertexNum, EdgeNum = map(int, sys.stdin.readline().split())
Vertex = [[] for _ in range(VertexNum + 1)]  # 1 <= Vertex <= 1000
check = [False] * (VertexNum + 1)
NumOfComp = 0

for _ in range(EdgeNum):
    FromEdge, ToEdge = map(int, sys.stdin.readline().split())
    Vertex[FromEdge].append(ToEdge)
    Vertex[ToEdge].append(FromEdge)

for i in range(1, VertexNum+1):
    if check[i] is False:
        dfs(i)
        NumOfComp += 1

print(NumOfComp)
