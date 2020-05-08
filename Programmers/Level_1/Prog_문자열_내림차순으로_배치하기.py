"""
    @ 프로그래머스 : 문자열 내림차순으로 배치하기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12917
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(s):
    return "".join(sorted(s, reverse=True))


s = "Zbcdefg"
print(solution(s))

