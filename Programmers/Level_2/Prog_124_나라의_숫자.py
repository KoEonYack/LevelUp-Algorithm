"""
    @ 프로그래머스 : 124 나라의 숫자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12899
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 12.
    @ End day: 20. 05. 12.
"""


def solution(n):
    ans = ""
    while n > 0:
        if n % 3 == 1:
            ans = "1" + ans
        elif n % 3 == 2:
            ans = "2" + ans
        elif n % 3 == 0:
            ans = "4" + ans
            n -= 1
        n = n // 3
    return ans


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(10))