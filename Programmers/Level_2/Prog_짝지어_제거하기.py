"""
    @ 프로그래머스 : 짝지어 제거하기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12973
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

from collections import deque

def solution(s):
    q = deque()

    for ch in s:
        if len(q) > 0 and q[-1] == ch:
            q.pop()
        else:
            q.append(ch)

    return 1 if len(q) == 0 else 0


s = "baabaa"
s = "cdcd"
print(solution(s)) # 1