"""
    @ 프로그래머스 : 최댓값과 최솟값
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12939
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(s):
    return str(min(list(map(int, s.split(" "))))) + " " + str(max(list(map(int, s.split(" ")))))

s = "1 2 3 4"
print(solution(s))