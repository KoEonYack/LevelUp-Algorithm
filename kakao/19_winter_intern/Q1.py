"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 크레인 인형뽑기 게임
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
     Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 20.
    @ End day: 20. 04. 20.
"""

def solution(board, moves):
    bucket = []
    ans = 0
    idx = -1

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                idx = board[i][move - 1]
                board[i][move - 1] = 0
                if len(bucket) > 0 and bucket[-1] == idx:
                    ans += 2
                    bucket.pop()
                else:
                    bucket.append(idx)
                break

    return ans


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
#        P 1 1 3 3 2 2
# moves = [1,5,3]

"""
board = [0,0,0,0,0],[0,0,1,0,0],[0,2,5,0,0],[4,2,4,4,2],[3,5,1,0,0]
moves = [0,4,2,4,0,1,0,3]
cache = [P,1,1,3,0,3,0,2]



"""


print(solution(board, moves)) # 4


