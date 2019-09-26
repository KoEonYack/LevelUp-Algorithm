def DFS(v):
    if n is v:
        global cnt
        cnt = cnt + 1
    else:
        for i in range(Map[v]):
            if Map[v][i] is 1 and ch[i] is 0:
                ch[i] = 1
                DFS(Map[v][i])
                ch[i] = 0


n, m = map(int, input().split())
Map = [[0] * 30 for _ in range(30)]
ch = [0] * 30
cnt = 0

for i in range(n):
    a, b = map(int, input().split())
    Map[a][b] = 1

ch[1] = 1
DFS(1)
print(cnt)