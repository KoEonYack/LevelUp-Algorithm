'''
    @ Baek 1759
    @ Prob. https://www.acmicpc.net/problem/1759
      Ref. https://statssy.github.io/pro/2019/09/09/baekjoon_1759/
      Ref Prob.
    @ Algo: Backtracking
    @ Start day: 19. 12. 17
    @ End day: 19. 12. 18
'''

def check(combStr):
    vowel = 0
    consonant = 0

    for char in combStr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1

    if consonant >= 2 and vowel >= 1:
        return True
    else:
        return False


def solution(L, inputList, combStr, index):

    if len(combStr) is L:
        if check(combStr) is True:
            print(''.join(combStr))
        return;

    if index >= len(inputList): # 프로그램 종료 조건
        return;

    solution(L, inputList, combStr+list(inputList[index]), index + 1)
    solution(L, inputList, combStr, index + 1)


answer = 0
L, C = map(int, input().split())
inputList = list(map(str, input().split()))
inputList.sort()

combStr = []
index = 0

solution(L, inputList, combStr, index)


