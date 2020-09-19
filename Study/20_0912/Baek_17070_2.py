
def dfs(x, y, z):  # → 0, ↘ 1, ↓ 2
    global k

    if x == n - 1 and y == n - 1: k += 1

    if z == 0 or z == 1:  # 파이프 방향 확인
        if y + 1 < n:  # 맵을 넘지 못하게 설정
            if D[x][y + 1] == 0:  # 칸에 벽이 없는지 확인
                dfs(x, y + 1, 0)

    if z == 0 or z == 1 or z == 2:
        if x + 1 < n and y + 1 < n:
            if D[x + 1][y] == D[x][y + 1] == D[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 1)

    if z == 1 or z == 2:
        if x + 1 < n:
            if D[x + 1][y] == 0:
                dfs(x + 1, y, 2)


n = int(input())
D = [[*map(int, input().split())] for _ in range(n)]
k = 0
dfs(0, 1, 0)
print(k)
