'''
    @ 66. 경로탐색
    @ Idea. DFS
    @ TestCase:
5 8
1 2 12
1 3 6
1 4 10
2 3 2
2 5 2
3 4 3
4 2 2
4 5 5
    @ output: 6
    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''


def DFS(v, sum):
    if v is n:
        global cost
        if cost > sum:
            cost = sum
    else:
        for i in range(1, m+1): # 1 ~ m
            if ch[i] is 0 and MapArr[v][i] > 0:
                ch[i] = 1
                #print(sum+MapArr[v][i])
                DFS(i, sum+MapArr[v][i])
                ch[i] = 0

MapArr = [[0] * 30 for _ in range(30)]
ch = [0] * 30
n, m = map(int, input().split())
cost = 999999

for i in range(m):
    a, b, w = map(int, input().split())
    MapArr[a][b] = w
print(MapArr)
ch[1] = 1
DFS(1, 0)
print(cost)