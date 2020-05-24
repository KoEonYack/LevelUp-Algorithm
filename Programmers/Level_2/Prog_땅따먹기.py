"""
    @ 프로그래머스 : 땅따먹기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12913
      Ref.
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 05. 12.
    @ End day: 20. 05. 12.
"""


def solution(land):

    DP = [[0]*4 for _ in range(len(land))]

    for i in range(4):
        DP[0][i] = land[0][i]

    for i in range(1, len(land)):
        for j in range(4):
            DP[i][0] = max(DP[i-1][1], DP[i-1][2], DP[i-1][3]) + land[i][0]
            DP[i][1] = max(DP[i-1][0], DP[i-1][2], DP[i-1][3]) + land[i][1]
            DP[i][2] = max(DP[i-1][0], DP[i-1][1], DP[i-1][3]) + land[i][2]
            DP[i][3] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2]) + land[i][3]

    return max(DP[-1])


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land)) # 16