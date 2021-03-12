'''
    @ 타겟넘버 [TODO]
    @ Prob. https://www.welcomekakao.com/learn/courses/30/lessons/43165
      Ref. https://lkhlkh23.tistory.com/74
    @ Algo: DFS
    @ Start day: 19. 09. 05
    @ End day:
'''
import sys
sys.setrecursionlimit(1000000)

def dfs(numbers, target, idx, num):
    if (num is len(numbers)) or (idx is 5):
        return 1 if num is target else 0
    else:
        return dfs(numbers, target, idx+1, num + numbers[idx]) + dfs(numbers, target, idx+1, num - numbers[idx])

def solution(numbers, target):
    return dfs(numbers, target, 0, 0)

a = [1, 1, 1, 1, 1]
print(solution(a, 3))
