"""
    @ 18 Summer winter coding: 점프와 순간이동
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12980
      Ref.
      Ref Prob.
    @ Algo: BFS
    @ Start day: 20. 05. 04.
    @ End day: 20. 05. 04.
"""

from collections import deque


def solution(n): # n : 종료지점
    ans = 0
    while True:
        if n in [1, 2]:
            ans += 1
            return ans
        if n % 2 == 1:
            n -= 1
            ans += 1
        n = n // 2


print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 2