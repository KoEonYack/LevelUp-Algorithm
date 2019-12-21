'''
    @ Baek 1405
    @ ISSUE : Time Error
    @ Prob. https://www.acmicpc.net/problem/1405
      Ref.
            https://kswims.tistory.com/173
            https://www.crocus.co.kr/678
      Ref Prob.
    @ Algo: Backtracking
    @ Start day: 19. 12. 18
    @ End day: 19. 12. 19
'''


def check(N, combStr):
    MAP = [[0] * (N * 2 + 1) for _ in range(N * 2 + 1)]
    i, j = N, N
    MAP[i][j] += 1

    for char in combStr:
        if char == "E":
            j -= 1
            MAP[i][j] += 1

            if MAP[i][j] > 1:
                return False;

        elif char == "W":
            j += 1
            MAP[i][j] += 1
            if MAP[i][j] > 1:
                return False;

        elif char == "S":
            i -= 1
            MAP[i][j] += 1
            if MAP[i][j] > 1:
                return False;

        elif char == "N":
            i += 1
            MAP[i][j] += 1
            if MAP[i][j] > 1:
                return False;

    return True;


def prob(combStr):
    global answer
    prob = 1
    for char in combStr:
        if char == 'E':
            prob = prob * percent[0]
        elif char == "W":
            prob = prob * percent[1]
        elif char == "S":
            prob = prob * percent[2]
        elif char == "N":
            prob = prob * percent[3]
    #print(prob)
    answer += prob
    return;

def solution(Length, combStr):

    if len(combStr) == Length:
        #print(combStr)
        if check(Length, combStr) is True:
            #print("[" + combStr + "]")
            prob(combStr)
        return;

    solution(Length, combStr+"E")
    solution(Length, combStr+"W")
    solution(Length, combStr+"S")
    solution(Length, combStr+"N")


N, e, w, s, n = list(map(int, input().split()))
combStr = ""
answer = 0
percent = [e/100, w/100, s/100, n/100]
solution(N, combStr)
print(answer)

