'''
    @ 76. 이항게수
    @ Idea. Recursive
    @ TestCase:
    @ Start day: 19. 11. 30.
    @ End day: 19. 11. 30.
'''
import sys
sys.setrecursionlimit(100000)

def dfs(m, n):
    #if Memory[m][n] > 0:
    #    return Memory[m][n]
    print(m, n)
    if m is n or n is 0:
        return 1
    else:
        #Memory[m][n] = dfs(m - 1, n - 1) + dfs(m - 1, n)
        #return Memory[m][n]
        return dfs(m - 1, n - 1) + dfs(m - 1, n)

m, n = map(int, input().split())
Memory = [[0]*21 for _ in range(21)]


print(dfs(m, n))