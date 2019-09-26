'''
    @ 65. 미로탐색
    @ Idea. BFS
    @ TestCase:
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
    @ output: 8
    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''

def DFS(x, y):
    if x == 7 and y == 7:
        global cnt
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if xx<1 or xx>7 or yy<1 or yy>7:
                continue
            if Map[xx][yy] is 0 or ch[xx][yy] is 0:
                ch[xx][yy] = 1
                DFS(xx, yy)
                ch[xx][yy] = 0


Map = [[] for _ in range(10)]
dx = [-1, 0, 1,  0]
dy = [ 0, 1, 0, -1]
ch = [[0]*10 for _ in range(10)]
cnt = 0
for i in range(7):
    Map[i] = map(int, input().split())

ch[1][1] = 1
DFS(1, 1)
print(cnt)