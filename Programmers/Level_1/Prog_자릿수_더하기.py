"""
    @ 프로그래머스 : 자릿수 더하기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12931
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""


def solution(n):
    return sum([int(i) for i in str(n)])


def sum_digit(number):
    return sum(map(int, str(number)))

N = 123
print(solution(N))