'''
    SWEA-1219-BFS
    Prob: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE

'''

queue = [0] * 1001
visit = [0] * 100
alen = [0] * 100
adj = [[col for col in range(100)] for row in range(2)]

# tc : test case
#for tc in range(10):
for tc in range(1):
    tn, n = input().split()
    tn = int(tn)
    n = int(n)

    while n is not 0:
        n = n - 1
        vertex_from, vertex_to = input().split()
        vertex_from, vertex_to = int(vertex_from), int(vertex_to)
        adj[alen[vertex_from]][vertex_from] = vertex_to
        alen[vertex_from] = alen[vertex_from] + 1

    re = fr = 0

    queue[re] = 0
    re = re + 1
    visit[0] = tc

    isEnd = False

    while re is not fr:
        now = queue[fr]
        fr = fr + 1

        if now is 99:
            isEnd = True
            break

        for i in range(alen[now]):
            next = adj[i][now]
            if visit[next] is tc:
                continue
            visit[next] = tc
            queue[re] = next
            re = re + 1

    print("# {0} {1}".format(tc, isEnd))

