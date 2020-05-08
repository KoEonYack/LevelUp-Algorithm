"""
    @ 프로그래머스 : 올바른 괄호
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12909
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
        if len(q) > 0 and q[-1] == "(" and ch == ")":
            q.pop()
        elif len(q) > 0 and q[-1] == ")" and ch == "(":
            return False
        else:
            q.append(ch)

    return len(q) == 0

s = "()()"
print(solution(s))