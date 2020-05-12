"""
    @ 프로그래머스 : 숫자의 표현
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12924
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 05. 12.
    @ End day: 20. 05. 12.
"""


def solution(n):

    ans = 0
    for i in range(1, n//2+2):
        s = 0
        for j in range(i, n//2+2):
            s += j
            if s == n:
                ans += 1
            elif s > n:
                break

    return ans + 1


print(solution(15))
