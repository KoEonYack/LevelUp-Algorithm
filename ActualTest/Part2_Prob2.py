'''
    Part2 - Prob2. : Step Magic

    [Condition]
    - 입력 범위 설정: 1*1 ~ N*N 같은 크기
    - D: down 1 step  D
    - L: right 1 step L
    - R: left 1 step  R
    - B: first-down 1 step, second 2 step. B
    Input Array Range : 5 ~ 1000
'''

def solution(arr):
    X = len(arr[0]) # 가로 갯수
    Y = len(arr)    # 세로 갯수

    answer = 0
    starNum = 0
    y = 0
    startX = 0
    for x in range(X):
        startX = x
        print("x", x)
        while True:
            #print(x, y)
            if arr[y][x] == 'D':
                y += 1
            elif arr[y][x] == 'R':
                x += 1
            elif arr[y][x] == 'L':
                x -= 1
            elif arr[y][x] == 'S':
                if starNum == 0:
                    if y == (Y-1): # *일 때도 답이 된다.
                        y = 0
                        answer += 1
                        break
                    y += 1
                    starNum += 1
                elif starNum == 1:
                    starNum = 0
                    break
            if y == (Y-1):
                #print("Answer", x, y, "startX", startX) # DEBUG
                if arr[y][x] == 'D':
                    y = 0
                    answer += 1
                    break
                else:
                    y = 0
                    break
    return answer

print(solution("DDDDDD"))