'''
    @ 2389 Lack Counting
    @ Prob. 프로그램이 콘테스트 47p
    @ Algo: DFS
    @ Start day: 19. 09. 10
    @ End day:
'''


def dfs(x, y):
    map[x][y] = '.'

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < M and map[nx][ny] is 'W':
                dfs(nx, ny)

def solve():
    ans=0
    for i in range(N):
        for j in range(M):
            if map[i][j] is 'W':
                dfs(i, j)
                ans += 1
    print(ans)

map = [['W', '.', '.', 'W', 'W'],
       ['.', 'W', '.', '.', 'W'],
       ['.', 'W', '.', '.', 'W']]
N = len(map)
M = len(map[0])
solve()