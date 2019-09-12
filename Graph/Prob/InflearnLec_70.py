'''
    @ 그래프 최단거리
    @ Prob. https://www.inflearn.com/course/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/lecture/18259
      Ref.
    @ Algo: BFS
    @ Start day: 19. 09. 05
    @ End day: 19. 09. 05
'''
import queue
Q = queue.Queue()

data = [[6, 9],
        [1, 3],
        [1, 4],
        [2, 1],
        [2, 5],
        [3, 4],
        [4, 5],
        [4, 6],
        [6, 2],
        [6, 5]]
ch = [0] * 30

n, m = 6, 9 # m: 입력받는 라인 갯수, n : Vertex의 갯수
map = [[] for i in range(30)]
dis = [0] * 30

for i in range(m):
    map[data[i][0]].append(data[i][1])

Q.put(1) # Vertex 1번을 큐에 집어 넣는다.
ch[1] = 1
while Q.empty() is not True:
    x = Q.get()
    for i in range(len(map[x])):
        if ch[map[x][i]] is 0:
            ch[map[x][i]] = 1
            Q.put(map[x][i])
            dis[map[x][i]] = dis[x] + 1

for i in range(2, n):
    print("{0} : {1}".format(i, dis[i]))