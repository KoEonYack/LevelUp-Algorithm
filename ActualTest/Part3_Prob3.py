'''
    Part3 - Prob3. : DFS
    minaArr[y][x] : y, x축 좌표
'''


dx = [ 0, 0,  1, 1, 1, -1, -1, -1]
dy = [-1, 1, -1, 0, 1, -1,  0,  1]


def solution(N, mineArr, Pos):
    ans = 0
    MAP = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(mineArr)):
        y, x = mineArr[i]
        y, x = y-1, x-1

        MAP[y][x] = '*'

    # 지뢰 및 숫자 설정
    for yy in range(len(MAP)):
        for xx in range(len(MAP[0])):
            if MAP[yy][xx] == '*': # 지뢰를 발견한 경우
                for i in range(8): # 상하좌우를 살펴보자
                    # 상하좌우가 맵을 벗어나지 말아야한다.
                    x = xx + dx[i]
                    y = yy + dy[i]
                    if x >= 0 and y >= 0 and x < N and y < N and MAP[y][x] != '*':
                        MAP[y][x] += 1

    # BFS


    # 현재 상황 출력
    '''
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            print(MAP[i][j], end=" ")
        print()
    '''

    # 출력 결과
    for i in range(len(mineArr)):
        if mineArr[i] == Pos: # 입력 좌표가 지뢰일 때
            print("Bomb")
            return 1

    return ans


print(solution(9, [[1,2],[2,6],[3,4],[3,8],[4,9],[5,4],[5,8],[6,7],[7,2],[9,1]], [9,1]))

