'''
    @ 64. 경로탐색
    @ Idea. DFS
    @ TestCase:
5 9
1 2
1 3
1 4
2 1
2 3
2 5
3 4
4 2
4 5
    @ Start day: 19. 09. 25
    @ End day: 19. 09. 25
'''


def DFS(v):
    if v == FindNode:
        global check
        check += 1
        return
    else:
        for i in range(1, FindNode+1): # 1 ~ FindNode
            if mapArr[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0


mapArr = [[0] * 30 for _ in range(30) ]
ch = [0] * 30
check = 0
FindNode, vertexNum = map(int, input().split())
for _ in range(vertexNum):
    i, j = map(int, input().split())
    mapArr[i][j] = 1

ch[1] = 1
DFS(1)

print(check)