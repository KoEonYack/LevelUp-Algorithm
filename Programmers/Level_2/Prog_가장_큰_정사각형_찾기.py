"""
    @ 프로그래머스 : 124 나라의 숫자
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/12899
      Ref.  https://i-am-wendy.tistory.com/13
      Ref Prob.
    @ Algo: DP
    @ Start day: 20. 05. 12.
    @ End day: 20. 05. 12.
"""


def solution(board):

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1

    return max([pow(num, 2) for row in board for num in row])


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
print(solution(board)) # 9



