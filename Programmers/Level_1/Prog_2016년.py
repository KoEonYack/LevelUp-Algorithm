"""
    @ 프로그래머스 : 2016년
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12901
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

from datetime import date

def solution(a, b):
    Week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return Week[date(2016, a, b).weekday()]

a = 5
b = 24
print(solution(5, 24)) # TUE

