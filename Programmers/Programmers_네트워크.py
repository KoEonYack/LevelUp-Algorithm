'''
    @ 네트워크 [TODO]
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/43162
      Ref.
    @ Algo: DFS
    @ Start day: 19. 09. 04
    @ End day:
'''
import sys
sys.setrecursionlimit(1000000)

def dfs(x, computers):
    check[x] = True
    for i in computers[x]:
        if (computers[x][i] is 1):
            if (check[i] is False): # 존재하는 vertex 라면
                dfs(x, computers)

def solution(n, computers):
    answer = 0

    for i in range(n):
        if check[i] is False:
            dfs(i, computers)
            answer += 1

    return answer

check = [False] * 4
result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(check)
print(result)