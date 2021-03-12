'''
    @ SWEA-1219-DFS
    @ Prob: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE
    @ Algo: DFS
    @ Start Day: 19.09.01
    @ Sov Day: 19.09.02
'''

a = []
b = []
result = 0

def dfs(now):
    if (a[now] is 99) or (b[now] is 99):
        global result
        result = 1
        return
    else:
        if a[now] != -1: # a[now]에 저장된 값이 now하고 인접한 vertex가 된다.
            dfs(a[now])
        if b[now] != -1:
            dfs(b[now])

TotalTestSetNum = 1
while TotalTestSetNum is not 0:
    TotalTestSetNum = TotalTestSetNum -1
    result = 0
    setNum, vertexSetNum = input().split()

    a = [-1] * 100
    b = [-1] * 100

    setNum = int(setNum)
    vertexSetNum = int(vertexSetNum)

    for i in range(vertexSetNum):
        fromVertex, toVertex = input().split()
        fromVertex = int(fromVertex)
        toVertex = int(toVertex)

        if a[fromVertex] == -1:
            a[fromVertex] = toVertex
        else:
            b[fromVertex] = toVertex

    dfs(0)
    print("# {0} {1}".format(setNum, result))