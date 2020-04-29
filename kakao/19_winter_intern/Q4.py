"""
    @ 2019 카카오 개발자 겨울 인턴십 코딩 테스트 : 징검다리 건너기
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/64062
     Ref.   https://tech.kakao.com/2020/04/01/2019-internship-test/
    @ Algo: 구현
    @ Start day: 20. 04. 27.
    @ End day: 20. 04. 27.
"""

import copy

INF = 200000000

def solution(stones, k):
    left = 1; right = INF

    while left <= right:
        mid = (left + right) // 2
        tmp = copy.deepcopy(stones)
        for i in range(len(tmp)):
            tmp[i] -= mid

        cnt = 0
        check = False
        for i in range(len(tmp)):
            if tmp[i] <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                check = True
                break

        if check is True:
            right = mid - 1
        else:
            left = mid + 1

    return left


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
print(sorted(stones))
k = 3
print(solution(stones, k)) # 3


