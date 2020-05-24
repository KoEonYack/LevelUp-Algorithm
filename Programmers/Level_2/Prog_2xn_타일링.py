"""
    @ 프로그래머스 : 2 x n 타일링
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12900
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 05. 12.
    @ End day: 20. 05. 12.
"""

def solution(n):
    mod = 1000000007
    DP = [0, 1, 2] + [0] * 60000
    for i in range(3, len(DP)):
        DP[i] = (DP[i-1] + DP[i-2]) % mod
    return DP[n]


print(solution(4)) # 5