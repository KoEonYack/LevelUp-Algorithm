'''
    @ Max of Land
    @ Prob. https://github.com/codingstudy-pushup/javacoding_top50/blob/master/MaxOfIsland.java
      Ref.
    @ Algo: DFS
    @ Start day: 19. 09. 05
    @ End day: 19. 09. 05
'''

def dfs(grid, x, y, area):
    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] is 0:
        return area
    grid[x][y] = 0
    area += 1
    for i in range(len(dirs)):
        area = dfs(grid, x+dirs[i][0], y+dirs[i][1], area)
    return area

def maxAreaOfIsland(grid):
    if (grid is None) or (len(grid) is 0):
        return 0

    maxV = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] is 1:
                area = dfs(grid, i, j, 0)
                print("area: ", area)
                maxV = max(area, maxV)

    return n

grid = [[1, 1, 0, 1, 1],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1]]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
m = len(grid)
n = len(grid[0])
print(maxAreaOfIsland(grid))