"""
    @ 프로그래머스 : 다음 큰 숫자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12911
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(n):
    num_of_one = bin(n).count("1")

    while True:
        n += 1
        if bin(n).count("1") == num_of_one:
            return n


n = 15
print(solution(n))