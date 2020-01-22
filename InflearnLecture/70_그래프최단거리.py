'''
    @ 70. 그래프 최단거리
    @ Idea. BFS
    @ Start day: 19. 11. 30
    @ End day: 19. 11. 30 / 20. 01. 22
'''

Map = [[] for i in range(30)]
Q = []
ch = [0] * 30
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
    for i in range(len(Map[x])):
        if ch[Map[x][i]] == 0:
            ch[Map[x][i]] = 1
            Q.append(Map[x][i])
            dis[Map[x][i]] = dis[x] + 1

for i in range(2, n+1): # 2 ~ n
    print("{0} : {1}".format(i, dis[i]))

"""
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
>
2 : 3
3 : 1
4 : 1
5 : 2
6 : 2
"""