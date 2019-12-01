'''
    @ 70. 그래프 최단거리
    @ Idea. BFS
    @ TestCase:
6 9
1 3
1 4
2 1
2 5
3 4
4 5
4 6
6 2
6 5
    @ Start day: 19. 11. 30
    @ End day: 19. 11. 30
'''

Map = [[] for i in range(30)]
ch = [0] * 30
Q = []
dis = [0] * 30
n, m = map(int, input().split())

for i in range(m):
    a, b = map(int, input().split())
    Map[a].append(b)

Q.append(1)
ch[1] = 1

while len(Q) is not 0:
    x = Q[0]
    Q.pop(0)
    print(Q)
    for i in range(len(Map[x])):
        if ch[Map[x][i]] == 0:
            ch[Map[x][i]] = 1
            Q.append(Map[x][i])
            dis[Map[x][i]] = dis[x] + 1

for i in range(2, n+1): # 2 ~ n
    print("{0} : {1}", i, dis[i])
