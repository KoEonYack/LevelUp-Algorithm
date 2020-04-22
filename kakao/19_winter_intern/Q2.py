"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 :튜플
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64065
     Ref.
    @ Algo: 구현
    @ Start day: 20. 04. 22.
    @ End day: 20. 04. 22.
"""

def solution(S):
    S = S[2:-2].split("},{")
    numArr = []
    print(S)
    for i in range(len(S)):
        numArr.append(set(S[i].split(",")))

    numArr.sort(key=lambda x: len(x))

    res = []
    ans = set()
    for a in numArr:
        tmp = a - ans
        res.append(list(tmp)[0])
        ans = ans | tmp

    res = [int(i) for i in res]
    return res



# S = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# print(solution(S)) # [2, 1, 3, 4]

S = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(S)) # [2, 1, 3, 4]


S = "{{123}}"
print(solution(S)) # [123]

S = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(S)) # [3, 2, 4, 1]

