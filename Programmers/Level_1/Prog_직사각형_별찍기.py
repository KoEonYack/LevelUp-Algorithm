"""
    @ 프로그래머스 : 직사각형 별찍기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12969
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

a, b = map(int, input().strip().split(' '))
print("\n".join(['*'*a for _ in range(b)]))