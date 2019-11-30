'''
    Part3 - Prob3. : DFS
    minaArr[y][x] : y, x축 좌표
'''


xArr = [0, -1, 0, 1]
yArr = [1, 0, -1, 0]

def solution(N, mineArr, P):
    ans = 0
    MAP = [['0' for _ in range(N)] for _ in range(N)]

    for i in range(len(mineArr)):
        y, x = mineArr[i]
        y, x = y-1, x-1

        MAP[y][x] = '*'

    for yy in range(len(mineArr)):
        for xx in range(len(mineArr[0])):
            if mineArr[yy][xx] == '*': # 지뢰를 발견한 경우
                for i in range(len(xArr)): # 상하좌우를 살펴보자
                    # 상하좌우가 맵을 벗어나지 말아야한다.
                    if xx + xArr[i] >= 0 and yy + yArr[i] >= 0 and xx + xArr[i] < N and yy + yArr[i] < N:
                        MAP[yy][xx] += 1

    for i in range(len(MAP)):
        print(MAP[i])

    return ans


print(solution(9, [[1,2],[2,6],[3,4],[3,8],[4,9],[5,4],[5,8],[6,7],[7,2],[9,1]], [8,5]))

