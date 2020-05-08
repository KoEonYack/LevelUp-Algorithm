"""
    @ 프로그래머스 : 체육복
    @ Prob. https://programmers.co.kr/learn/courses/30/lessons/42862
      Ref.
      Ref Prob.
    @ Algo: 구현
    @ Start day: 20. 05. 08.
    @ End day: 20. 05. 08.
"""

def solution(n, lost, reserve):
    reserve_arr = reserve
    lost_arr = lost

    for num in reserve_arr:
        if num in lost:
            lost_arr.remove(num)
        elif num-1 in lost:
            lost_arr.remove(num-1)
        elif num+1 in lost:
            lost_arr.remove(num+1)

    return n - len(lost_arr)

n = 5
lost = [2, 4]
revserve = [1, 3, 5]
revserve = [3]
print(solution(n, lost, revserve))
