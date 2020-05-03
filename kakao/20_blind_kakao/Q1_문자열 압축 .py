"""
    @ 2020 카카오 블라인드 리쿠르트 테스트 : 문자열 압축
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/60057
     Ref.
    @ Algo: 구현
    @ Start day: 20. 05. 02.
    @ End day: 20. 05. 02.
"""

def solution(s):
    if len(s) == 1: return 1
    minV = 999999

    for div in range(1, len(s) // 2 + 1):
        result = ""
        cnt = 1
        divStr = s[:div]
        for i in range(div, len(s), div):
            if s[i:i+div] == divStr:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                result += str(cnt) + divStr
                divStr = s[i:i+div]
                cnt = 1
        if cnt == 1:
            cnt = ""
        result += str(cnt) + divStr

        if minV > len(result):
            minV = len(result)

    return minV


s = "aabbaccc"
print(solution(s)) # 7
#
# s = "ababcdcdababcdcd"
# print(solution(s)) # 9
