'''
    @ Baek 2661
    @ Prob. https://www.acmicpc.net/problem/2661
      Ref.
            https://suriisurii.tistory.com/17
      Ref Prob.
    @ Algo: Backtracking
    @ Start day: 19. 12. 19
    @ End day: 19. 12.
'''

finish = False

def Check(str):
    #print(str)
    start = len(str) - 1
    end = len(str)

    for i in range(1, int(len(str) / 2) + 1):
        firstStr = str[start - i: end - i]
        secondStr = str[start: end]
        #print(firstStr, secondStr)
        if firstStr == secondStr:
            return False;
        start -= 1

    return True;


def solution(len, str):
    global finish

    if finish:
        return;

    if Check(str) == False:
        return

    if len is N:
        # print("here")
        finish = True
        #if Check(str) is True:
        print(str)
        return;

    solution(len+1, str + "1")
    solution(len+1, str + "2")
    solution(len+1, str + "3")

    return;


N = int(input())
solution(1, "1")