'''
    @ 66. 경로탐색
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
    @ output: 6
    @ Start day: 19. 09. 26
    @ End day: 19. 09. 26
'''
import sys
sys.setrecursionlimit(1000000)

def DFS(v):
    if v is n:
        global check
        check += 1
    else:
        for i in range(len(MapArr[v])):
            if ch[MapArr[v][i]] is 0:
                ch[MapArr[v][i]] = 1
                DFS(MapArr[v][i])
                ch[MapArr[v][i]] = 0


n, m = map(int, input().split())
MapArr = [[] for i in range(30)]
ch = [0] * 30
check = 0
for i in range(m):
    print(MapArr)
    a, b = map(int, input().split())
    MapArr[a].append(b)

ch[1] = 1
DFS(1)
print(check)
