'''
    @ 1697. 숨바꼭질
    @ Prob. https://www.acmicpc.net/problem/1697
     Ref. https://jun-itworld.tistory.com/19?category=778547
    @ Algo: BFS
    @ Start day: 19. 09. 03
    @ End day:
'''

def bfs(N, M):
    time = 0
    q = []
    q.append(N)

    while True:
        size = len(q)

        for i in range(size):
            n = q[0]
            q.remove(n)

            if n is M:
                return time
            if n>0 and visit[n-1] is 0:
                q.append(n-1)
                visit[n-1] = 1
            if n < 100000 and visit[n+1] is 0:
                q.append(n+1)
                visit[n+1] = 1
            if n*2 <= 100000 and visit[n*2] is 0:
                q.append(n*2)
                visit[n*2] = 1
        time += 1


#N : 수빈이가 있는 위치, M: 동생이 있는 위치
N, M = map(int, input().split())
visit = [0] * 100001
print(bfs(N, M))


