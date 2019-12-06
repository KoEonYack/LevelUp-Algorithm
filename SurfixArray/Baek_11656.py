'''
    @ Baek 11656
    @ Prob. https://www.acmicpc.net/problem/11656
      Ref. https://kks227.blog.me/221028710658
    @ Algo: 접미사 배열
    @ Start day: 19. 12. 09
    @ End day: 19. 12. 09
    @ Memo : Sort 함수:	O(N Log N)
'''


def solution(inputStr):
    AnsArr = []

    for i in range(len(inputStr)):
        AnsArr.append(inputStr[i:])
    AnsArr.sort()
    return AnsArr

arr = solution("baekjoon")
for a in arr:
    print(a)


